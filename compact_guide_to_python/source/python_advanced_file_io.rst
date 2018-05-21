Files - the naked truth
=======================

Your operating system handles file access for programs (you do not know whether
data is stored on a harddisk, SSD, magnetic tape or whatever). Reading from any
OS-level file object returns data from a stream of bytes (integer numbers in
the range from 0-255, a so-called *binary stream*)

.. admonition:: Important

   At the lowest level, the data takes the form of a bytes sequence independent
   of your idea of the content (video, sound, email, text document, pdf).
   Everything else is interpretation of the data: a paint-like program may
   decide to interpret the bytes read as the description of pixels to draw on
   the screen, while a word processor may interpret bytes as characters and
   accompanying formatting instructions.


Python's binary mode for file access
------------------------------------

You can ask Python to give you access to this stream of bytes by opening a
file in so-called *binary* mode (indicated by a 'b' attached to the mode
string).

.. admonition:: Try it:

   .. code:: python3

      i = open(r'C:\Windows\Web\Wallpaper\Theme2\img7.jmp','rb')
      data = i.read(20)
      print(data)

   Interesting, but these aren't integers between 0 and 255, are they?
   Well, kind of, but in disguise. Try:

   .. code:: python3

      for thing in data:
          print(thing)

   or:

   .. code:: python3

      list(data)   # or data[0], etc.

=> A bytes object, when asked for its elements returns integers 0-255 because
that is what it is made of. However when asked to show itself as a whole it
represents itself as hexadecimal code. Why: decimal 255 is hexadecimal FF so
every possible bytes value fits into two hexadecimal digits.


.. Note::

   In Python you can type any number not only in its decimal, but also in
   its hexadecimal form by prefixing it with ``0x``, *e.g.*:
   
   .. code:: python3
   
      a = 255
      b = 0xff
      
      print(a==b) # prints True because a and b are the same integer
      
   The built-in ``hex()`` function can convert a number into a string of
   its hexadecimal representation:
   
   .. code:: python3
   
      a = 255
      print(hex(a))    # => '0xff'
      

The ASCII code table for interpreting bytes as characters
---------------------------------------------------------

What about those characters inside data above?

One of the oldest standards in informatics is the *American Standard Code for
Information Interchange* (ASCII). It describes a standard mapping (called a
codepage) that allows the encoding of all English alphanumeric and punctuation
characters, and of some formatting control characters (like the newline and
tabulator character) as integer numbers between ``0`` and ``127``, *i.e.*,
using the first half of the range of bytes numbers. In ASCII, the printable
characters (as opposed to control characters) are encoded by the numbers ``32``
(0x20 in hexadecimal form) to ``126`` (0x7e).

When a bytes object gets displayed all its numbers from the ASCII printable
character range get displayed as the corresponding characters! This is very
useful because many files do contain at least some ASCII-encoded text.
So printing their bytes objects is a quick and simple way of inspecting such
data without knowing anything about it.

.. admonition:: Try it:

   .. code:: python3

      i = open(r'C:\Windows\explorer.exe', 'rb')
      data = i.read(120)
      print(data)

   Note the MS-DOS executable start bytes "MZ" (0x4d, 0x5a), the initials of
   Mark Zbikowski, one of the earliest MS developers, and the Warning message
   embedded into the file.

ASCII is a very important *codepage* to know because it is the basis of almost
all other existing text encoding schemes, which usually extend the ASCII table
with their own additional character mappings to the bytes range not used by
ASCII (128-255).

.. admonition:: Remember this about Python bytes

   A bytes object is a *sequence* (supporting all general Python sequence
   operations) of *integer* values between ``0`` and ``255``, which you can
   retrieve by asking for individual elements one by one. On output, the bytes
   object as a whole (or *slices* of it) gets formatted as a *bytes string*
   (a string prefixed with ``b``) of the hexadecimal representations of the
   numbers in the sequence. Numbers from the printable character range of the
   ASCII codepage (32-126), however, get formatted as their character
   representations.
   
   Example:
   ``b'\xff\xd8\xff\xee\x00\x0eAdobe\x00d\xc0\x00\x00\x00\x01\xff\xdb'``


Python's text mode for file access
----------------------------------

As we've seen above you can read *any* file using binary mode. So why is this
not enough?
The answer is that if what we are trying to access is really a text file than
we can do better than reading just the bytes andusing ASCII to print them.
Pure ASCII decoding is often insufficient for regular text because the 128 code
points that it defines are not enough for all the characters we want to
represent.

.. admonition:: Try it:

   .. code:: python3

      i = open(r'C:\bwLehrpool\Device_Optimization_Tool\INSTRUCTIONS.txt', 'rb')
      data = i.read()
      print(data)

   This may look like a minor problem for German text, but think of Chinese or
   Arabic text!

Many computer and software manufacturers have invented their own codepages that
extend ASCII and use the remaining 128 numbers that fit into one byte to
support special cases.

There are *many* such codepages and a text editor now needs to know what the
codepage used in a file is to decode the characters not defined by ASCII.

This is where default **text** mode of ``open()`` comes into play.
Just leave out the ``'b'`` from the mode and Python will interpret the bytes
sequence it gets from the operating system using an OS-dependent
bytes-to-character map!

.. admonition:: Try it:

   .. code:: python3

      i = open(r'C:\bwLehrpool\Device_Optimization_Tool\INSTRUCTIONS.txt', 'r')
      data = i.read()
      print(data)
      
      print(i.encoding)  # probably 'cp1252' aka Windows Western-Europe


If you think you know better than the operating system, you can specify the
encoding to use explicitly.

.. admonition:: Try it:

   Let's try the last example again using codepage 1256 (the standard Arabic
   codepage):

   .. code:: python3

      i = open(
              r'C:\bwLehrpool\Device_Optimization_Tool\INSTRUCTIONS.txt',
              'r',
              encoding='cp1256' # optional argument to open()
          )
      data = i.read()
      print(data)

   Still acceptable with only a few misinterpreted characters, but try with
   encoding='cp1255' (Hebrew), which does not define bytes->character mappings
   for some of the bytes in our file!


.. admonition:: Some encodings worth remembering:

   - latin1 (aka iso8859-1, cp819)

     an often-encountered encoding in the Windows world with the benefit that
     every byte has a character mapping, *i.e.*, when you open a file for
     reading and assume 'latin1' encoding, you may get some weird characters,
     but there won't be any errors
   
   - cp1252 (Windows Western-Europe)

     widespread in the Western-European Windows world (supports almost all
     characters typically found on any Western-European keyboard)

   - utf8 (the standard on Linux and macOS and the de facto modern standard in
     the world)
  
     can map almost any written character in any language of the world to
     bytes; the trick is that utf8 is a multi-byte encoding in which the
     characters not already defined by ASCII get encoded by more than one byte
     (which makes utf8 relatively expensive to process);
     
     not safe during reading: not every bytes sequence maps to a character!


Recommendations for opening files with Python
---------------------------------------------

- If you are only copying files and can live with the limitations, work in
  binary mode. This is the fastest way and it guarantees that you write the
  same bytes to disk that you are reading!

- If you are writing new files yourself and you have the choice, use "utf-8"
  encoding. Modern software will know how to deal with it!

- If you require fail-safe reading and you don't mind some misinterpreted
  characters use latin1, but don't make a habit out of it!

- A more sophisticated approach for reading files with unknown encoding is to
  open the file assuming utf8 encoding, then do your reading from the file
  inside a ``try``/``except`` block to catch any possible
  ``UnicodeDecodeError``. If such an error occurs, you know the file isn't
  utf8-encoded and can use latin1 as a fail-safe fallback.
  Here's an illustration of this approach:
  
  .. code:: python3
  
     assume_encoding = 'utf8'
     while True:
         i = open(some_file, encoding=assume_encoding)
         try:
             text = i.read()
         except UnicodeDecodeError:
             assume_encoding = 'latin1'
             continue
         break

Other file handling tips and tricks
===================================

- File objects opened in text mode do there counting in characters, binary file
  objects in bytes. This is the same for single-byte, but not for multi-byte
  encoding schemes like utf8.

- ``read()`` and friends return the empty string ``''`` when you've reached the
  end of a file. Use a corresponding check, *e.g.*, to break out of ``while``
  loops that read chunks of data.

- Use ``read()`` and ``readlines()`` with care and make use of their length
  argument if you are unsure about the input data size. Files don't necessarily
  fit into memory.

- Don't use ``readline()`` or ``readlines()`` blindly on true binary files.
  Such files just might not have a newline character in them so this would
  read the whole file at once again.
  
- Don't combine file iteration with ``readline()`` because the two use
  different buffers.
  
- Use tell() and seek() to hop around in files:

  .. code:: python3
  
     # for text mode files:
     seek(position_obtained_from_tell) -> rewind to a bookmarked position
     seek(0)                  -> rewind to beginning of file
     seek(0, 2)               -> jump to end of file
  
     # for binary mode files:
     seek(absolute_position_in_bytes)  -> as obtained from tell() or calculated
     seek(relative_to_current, 1)
     seek(relative_from_end, 2)      # e.g. seek(-10, 2)

-----

.. admonition:: Congratulations!

   You are far from being a beinner with Python-based file access now and
   should be able to process basically any electronically stored data you
   can get access to.
 
