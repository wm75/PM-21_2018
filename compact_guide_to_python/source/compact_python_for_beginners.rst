A compact guide to Python 3 - Beginner's level
==============================================

Arithmetics
-----------

.. code:: python3

    >>> 783 + 72  # addition
    855

    >>> 855 - 72  # subtraction
    783

    >>> 42 * 7    # multiplication
    294

    >>> 42 / 7    # division, result returned as floating point number
    6.0
    
    >>> 42 // 7   # floor division, result returned as integer number
    6
    
    >>> 47 // 7   # floor(!) division
    6
    
    >>> 47 % 7    # remainder of division
    5
    
    >>> 5 ** 3    # exponentiation
    125
    
    >>> (6 - 3) * 2**3  # standard operator precedence rules apply
    24
    
    # mixed integer and floating point operands give floating point result
    >>> 4 * 3.75 -1
    14.0


Logic operations
----------------

``True`` and ``False`` are Python's way to express the logical outcome of
comparisons and yes/no questions.

.. code:: python3

   >>> 5 > 3   # is 5 greater than 3?
   True
   
   >>> 5 < 3   # is 5 less than 3?
   False
   
   >>> 3 >= 3  # is 3 greater than or equal 3?
   True
   
   >>> 3 <= 3  # is 3 less than or equal 3?
   True
   
   >>> 3 == 3  # does 3 equal 3?
   True
   
   >>> 5 != 3  # does 5 NOT equal 3?
   True
   
.. admonition:: Caveats:

   The two-character comparison operators ``>=``, ``<=``, ``==`` and ``!=``
   have to be written *exactly* like this. Spaces between the characters,
   using them in a different order or combining them in other ways all cause
   ``SyntaxError``.
   
   The test for equality is done with the two-character ``==`` operator because
   the single ``=`` is used for assignments, *e.g.*,
   
   .. code:: python3
   
      >>> x = 5   # assign the integer 5 to x
      >>> x == 5  # test that x now equals 5
      True
      
Python can also evaluate the truthi-/falsiness of any object itself, *i.e.*,
without a comparison. This may sound weird, but is often very useful and
follows very simple, clear rules:

Any built-in Python object is considered truthy with the exception of:

   - ``None``   (the special object used to represent nothingsness in Python)
   - ``False``  (should be obvious; how could ``False`` be ``True``?)
   - any zero numbers (``0``, ``0.0``, *etc.*)
   - any sequence or collection of objects with zero length
     (this includes the empty string ``''`` and the empty list ``[]`` for
     example)

To trigger the truthi-/falsiness evaluation of an object, you can either

- use the built-in ``bool()`` function on the object, e.g.,

  .. code:: python3
  
     >>> bool(3)   # 3 is a number and it's not zero so ...
     True
     
     >>> bool([])  # an empty list has zero elements
     False
     
- use the object with ``if``, but without a comparison operator (in this case
  Python will call ``bool()`` for you to decide what to do). For example:
  
  .. code:: python3
  
     if data:
        # do something with the data here
        print(data)
     else:
        print('There is no data to process.')
  
  will print *There is no data to process.* whenever data is ``None``,
  ``False``, some sort of zero, or has zero elements.
  

Literals
--------

Objects can be created from literal representations, specifically:

- ``13``, ``0b1101``, ``0o15``, ``0xd`` can all be used to create an integer
  number object with the decimal value 13
  
- ``2.00``, ``2.0``, ``2.`` create a floating point number object with the
  value 2.0 (just like terminal zeros, a leading zero can be omitted, so
  ``0.75`` and ``.75`` are equivalent);
  you can also use scientific notation as in ``1.5e3`` (or equivalently,
  ``1.5e+3``) and ``1.5e-3``
  
- ``"Hello World"`` or ``'Hello World'`` create the `string`_ *Hello World*
  (whether you use single or double quotes is up to you, but having the choice
  simplifies the creation of strings that themselves contain one of the
  quote types, e.g., ``'I said: "Hello World"'``). An *empty string* literal
  consists only of quotes surrounding nothing (``''`` or ``""``). It generates
  a string object of zero characters.
  
- ``[1, 2, 3]`` creates a `list`_ of three integers (a comma after the last
  element is allowed, so ``[1, 2, 3,]`` is an equivalent literal);
  to create a list with just one element, you can use, *e.g.*, ``[1]`` or
  ``[1,]``; the literal for an empty list is ``[]``

- ``(1, 2, 3)`` or ``(1, 2, 3,)`` (trailing comma) creates a three-element
  `tuple`_;
  to create a single-element tuple, the trailing comma is obligatory as in
  ``(1, )`` (because ``(1)`` just represents the integer 1 in parentheses);
  the literal for an empty tuple is ``()``
  
- ``{1, 2, 3}`` is a three-element `set`_ literal; like for list literals a
  comma after the last element is allowed; a single-element set can be written
  as ``{1}`` or ``{1, }``; there is no empty set literal (**!!** ``{}`` is
  used to denote an empty dictionary **!!**)

- ``{"a": 1, "b": 2, "c: 3"}`` represents a `dictionary`_ with three key/value
  pairs; again, a comma after the last element (*i.e.*, the last pair) is
  allowed; ``{}`` is the empty dictionary literal
  

Conversion between object types
-------------------------------

Integer number objects can be generated from other types using the ``int()``
function, *e.g.* :

.. code:: python3

   >>> int("15")    # integer number from string
   15
   
   >>> int("15.0")  # string MUST represent an integer
   Traceback (most recent call last):
     File "<pyshell#40>", line 1, in <module>
       int("15.0")
   ValueError: invalid literal for int() with base 10: '15.0'
   
   >>> int(15.3)   # integer from floating point (decimal digits get truncated)
   15
   
-----

Floating point number objects can be generated from other types using the
``float()`` function:

.. code:: python3

   >>> float("3.1415")    # float object from string
   3.1415
   
   >>> float("31415e-4")  # float object from string in scientific format)
   3.1415
   
   >>> float(15)          # float object from integer
   15.0

-----

`Strings`_ can be generated from almost any object in Python. The ``str()``
function is a bit different from the other conversion functions because it asks
the object it is given to *represent* itself as a `string`_ and the object has
any freedom to do so. This makes ``str()`` very flexible, but sometimes also
surprising for beginners.

.. code:: python3

   >>> str(3)
   '3'
   
   >>> str(3.1415)
   '3.1415'

   >>> str(False)
   'False'
   
   >>> str(None)
   'None'
   
   >>> str([1,2,3,4,5])
   '[1, 2, 3, 4, 5]'
   
   >>> str(['a', 'b', 'c', 'd'])   # this does NOT concatenate
   "['a', 'b', 'c', 'd']"

If you want to concatenate strings stored in a `list`_ or other
*sequence*, use the `join method of strings`_ instead.

`String formatting`_ offers more control over string representations.

-----
   
`Lists`_, `tuples`_ and `sets`_ can be interconverted or generated from other
*sequence* types using correspondingly named functions:

.. code:: python3

   >>> list((1, 2, 3))    # list from tuple
   [1, 2, 3]
   
   >>> tuple([1, 2, 3])   # tuple from list
   (1, 2, 3)
   
   >>> set([1, 2, 2, 3])  # set from list (results in duplicate removal)
   {1, 2, 3}
   
   >>> list({1, 2, 3})    # list from set (result will have no guaranteed order)
   {1, 2, 3}
   
   >>> set('Hello World') # set from a string (duplicate removal)
   {'H', 'W', 'd', ' ', 'l', 'o', 'r', 'e'}

-----
   
`Dictionaries`_ can be generated from sequences of pairs of items:

.. code:: python3

   >>> dict([("a", 1), ("b", 2), ("c", 3)])  # from a list of 2-element tuples
   {'a': 1, 'b': 2, 'c': 3}
   
To convert a `dictionary`_ to a `list`_, `tuple`_ or `set`_, you have to decide
if you want just the *keys*, the *values*, or both converted:

.. code:: python3

   >>> d = {"a": 1, "b": 2, "c": 3}
   
   >>> list(d)  # a list from just the keys
   ['a', 'b', 'c']
   
   >>> tuple(d.values())  # a tuple from the values in the dictionary
   (1, 2, 3)
   
   >>> list(d.items())  # a list of key/value pairs converted to tuples
   [('a', 1), ('b', 2), ('c', 3)]
   
   
Assignment
----------

The assignment operator ``=`` creates the **identifiers** with the names
indicated to the left of the ``=`` and binds them to the objects that result
from the evaluation of everything on the right side of the ``=``. After the
assignment the identifiers can be used as aliases for their objects.

A simple assignment uses just one identifier and one object, like in these
examples:

.. code:: python3

   >>> x = 1.2 + 8*2

   >>> special_numbers = [2, 3, 3.1415, 12, 13, 42, 666, 1001]
   
The expression on the right side gets evaluated (to the float object ``17.2``
or a list object) and bound to the identifiers named ``x`` and
``special_numbers``, respectively. After that, these identifiers can be used
anywhere ``17.2`` or the list ``[2, 3, 3.1415, 12, 13, 42, 666, 1001]`` could
be used:

.. code:: python3

   >>> x - 3
   14.2
   
   >>> y = x // 2  # calculate 17.2 // 2 and assign the result (8.0) to y
   
   >>> x = x * x   # calculate 17.2*17.2 and assign the result back to x
   
   >>> x = x - 3
   292.84
   
   >>> set(special_numbers)
   {2, 3.1415, 3, 1001, 42, 12, 13, 666}
   

User Interaction
----------------

Use ``print()`` to display text on the screen:

.. code:: python3

   # diplay a simple string
   print("Hello User!")
   
   # print accepts any number of comma-separated Python objects.
   # Objects that are not strings, are first asked to format themselves as
   # strings (and often the result is just what you want).
   
   print(42, "divided by", 6, "is", 42//6)
   
Per default, when print gets passed multiple objects, they get separated by a
space in the output, and the output of each print command gets terminated by a
line break, but you can change this behavior by providing your own ``sep`` and
``end`` values in the form of keyword arguments following the objects to be
printed:

.. code:: python3

   print(42, 6, sep='/', end=' = ')
   print(42//6)
   
``input()`` can be used to capture a line of input typed on the keyboard.
This function will stop the execution of your code until it receives a complete
line of input (terminated by a line break, *i.e.*, the user hitting ``Enter``).
It returns the line (without the line break) as a string object. If you pass a
string to ``input()``, it is displayed (without any separator) before the
cursor that expects the user input.

.. code:: python3

   # get the user's name
   # The trailing space in the prompt string is necessary to prevent the typed
   # user input from getting joined to the prompt directly.
   user_name = input("What's your name? ")
   
   print("Hello", user_name)
   
   # if you do not want a string, but a different type of object, you have to
   # do the conversion yourself.
   
   user_age = int(input("How old are you? "))


Flow Control
------------

Repeated and/or conditional code execution is achieved through

- ``for`` and ``while`` loops, possibly with contained ``break`` and/or
  ``continue`` instructions
- ``if``/``elif``/``else`` constructs

In addition, the flow of a program can also be controlled by `raising and
handling exceptions`_ and, inside `functions`_, with ``return`` statements.

**Conditional execution with *if*/*elif*/*else***

.. code:: python3

   user_age = int(input("How old are you? "))
   
   if user_age < 0:
       print("Please come back after you are born.")
   elif user_age > 125:
       print("This content is for humans only.") 
   elif user_age < 18:
       print("We are sorry, but this content is for adults only.")
   else:
       print("Adult content!")

Conditional **repeated execution with *while***

.. code:: python3

   x = 2
   while x < 100:
       x = x*x
       # Note the first square value > 100 still gets printed
       print(x)
       
As an alternative to checking the condition on the first line, a common pattern
is to set up an endless loop and ``break`` out of it, when a condition is met.
Often this provides greater flexibility:

.. code:: python3

   x = 2
   while True:
       # This loop really stops printing when the first square > 100 is reached.
       x = x*x
       if x >= 100:
           break
       print(x)

**Looping over iterable objects with *for***

A line of the general form ``for item in object:`` initiates a block that
will loop over all elements contained in ``object`` provided that object is
iterable (a surprising lot of Python objects are). During each iteration of the
loop, the next element will be retrieved from ``object`` and is made accessible
through the identifier ``item`` (you can choose this name freely like that of
any other identifier).

.. code:: python3

   prime_product = 1
   for number in [2, 3, 7, 11, 13]:
       # iterate over the list of integer objects
       # Each time through the loop, the next element from the list will be
       # assigned to number.
       prime_product = prime_product * number
   print(prime_product)
   
   
   for c in "Hello World!":
       # strings are iterable objects yielding one character at a time
       if c.isalpha():
           # keep only letters
           # Printing is done with an empty string as the end character
           # so that we can join characters directly to each other.
           print(c, end='')
   print() # finish with a line break

The standard way to iterate over a regularly spaced sequence of numbers in
Python is to use a ``for`` loop over a `range`_.

.. _functions:

Functions
---------

Functions are blocks of code initiated with the keyword ``def``. The
instructions inside the block are executed whenever the function is *called*.
When the execution encounters a ``return`` statement the function terminates
and the object to the right of ``return`` is *"inserted"* instead of the
function call into the calling code. If execution of the function reaches the
end of the function's code block without encountering ``return``, the program
behaves as if it had encountered a ``return None`` instruction, *i.e.*, the
function call gets *"replaced"* with the ``None`` object in the calling code.

Defining a function (simple example):

.. code:: python3

   import random
   
   def dice_sum():
       """Roll two dice and return their sum.
       
       If both dice show the same number, double the sum.
       """
       roll1 = random.randrange(6) + 1
       roll2 = random.randrange(6) + 1
       result = roll1 + roll2
       if roll1 == roll2:
           result = 2 * result
       return result
	   
Calling it:

.. code:: python3

   print('Player #1 rolls the dice')
   
   # call the dice_sum function and assign whatever it returns to sum_player1
   # The parentheses after the function name indicate that we want the result
   # of the function (rather than the function object itself, which is also
   # possible) assigned.
   sum_player1 = dice_sum()
   
   print('Score of Player #1:', sum_player1)
   print('Player #2 rolls the dice')

   # call the dice_sum function again and assign whatever it returns to
   # sum_player2   
   sum_player2 = dice_sum()
   
   print('Score of Player #2:', sum_player2)

Functions with parameters
.........................

You can define functions that expect parameters by naming these inside the
parentheses in the function definition line:

.. code:: python3

   def linear_func(x, a, b):
       """Calculate the y value of a linear function at x.
       
       (x,y) is a point on a line defined by slope a and intercept b.
       """
       # This function has to be called with three objects as arguments.
       # Whatever these are, they will be accessible within the function
       # through the local (only known to our function) identifiers x, a and b.
       return a*x + b
       
Calling it:

.. code:: python3

   slope = 3
   intercept = -2
   x_values = [-1, 0, 1, 10]
   
   print(
       'Some points lying on a line with slope {0} and intercept {1}:'
       .format(slope, intercept)
       )
   for x in x_values:
       # call our function and use its return value directly for printing
       # x, slope and intercept are identifiers that refer to three different
       # integer objects. These objects (but not the identifiers) will be made
       # available to our function through the local identifier names it
       # defines in its definition line.
       print(x, linear_func(x, slope, intercept))


.. _raising and handling exceptions:

Exception Handling
------------------

Exceptions are Python's mechanism to signal exceptional events or conditions
that cannot be handled within the regular flow of the program. Exceptions can
be generated by Python and its built-in functions, *e.g.*:

.. code:: python3

   >>> int('Not every string can be interpreted as an integer')
   Traceback (most recent call last):
     File "<pyshell#7>", line 1, in <module>
       int('Not every string can be interpreted as an integer')
   ValueError: invalid literal for int() with base 10: 'Not every string can be interpreted as an integer'
   
but you can also generate them in your own code with a ``raise`` statement:

.. code:: python3

   def reject_inf(data_sequence):
       """Raise ValueError if data_sequence contains infinite values."""
       
       forbidden_values = [float('inf'), float('-inf')]
       for n in data_sequence:
           if n in forbidden_values:
               # raise an exception of type ValueError with an appropriate
               # message describing what happened
               raise ValueError('Sequence contains forbidden value ' + str(n))

   reject_inf([1,2,4,float('-inf'), 6])

Unhandled exceptions lead to interruption of normal control flow. Functions are
terminated at the point at which the exception occured and the calling code is
checked to see if it can handle the exception or not. This process continues
until a code block that handles the exception is found or until the outermost
code is reached at which point the program gets terminated.

Exception handling is done via ``try``/``except`` blocks like in this example:

.. code:: python3

   while True:
       user_input = input('Please enter an integer number: ')
       try:
           # See if we can turn the string obtained from the user into
           # an integer object.
           # Failure is indicated by an exception of type ValueError, which
           # we catch and deal with.
           n = int(user_input)
       except ValueError:
           # The user has entered something that cannot be interpreted as an
           # integer number. Let's start over
           print('Sorry, try again ...')
           continue
       # We got here, so we have an integer.
       # => no need to continue
       break

If an exception occurs anywhere in the ``try`` block, the ``except`` blocks
(yes, there can be several to deal with different exceptions) following it are
checked whether they accept the exception. If so, the corresponding block is
executed and (if it doesn't raise an exception itself) normal code execution
is resumed.

.. admonition:: Types of exceptions

   Some common *exceptions* that you should know and be able to interpret as a
   beginner are::

     TypeError   raised when code tries to use an object in a context,
                 in which an object type different from that of your
                 object is expected.
                  
                 Examples:
                   
                   10 + 'abc'  # cannot add objects of type int and str
                   
                   # only a sequence of strings can be joined
                   ', '.join([1,2,3])
                    
     ValueError  raised when code tries to use an object of appropriate
                 type, but with a value that cannot be dealt with in the
                 current context.
                 
                 Example:
                 
                   # the int() function can convert a string to an
                   # integer, but, for this to work, the string has to
                   # be interpretable as an integer
                   int('abc')
                   
                   # trying to get the position of a value in a sequence
                   # when that value is not present
                   
                   ['a', 'b', 'c'].index('d')
                   
                   
     IndexError  raised when code tries to access a position in a
                 sequence, but the position is higher than the highest
                 index in the sequence.
                 
                 Example:
                 
                   'short text'[10]


     KeyError    similar to IndexError, but raised when trying to access
                 an element by key (as for a dictionary).
                 
                 Example:
                 
                   d = {'a': 1, 'b': 2}
                   d['c']


Importing code from modules
---------------------------

.. code:: python3

   import math   # import the Python math module that is part of the stdlib
   
   # All objects defined in math can now be accessed through their
   # identifiers preceeded with math. as the namespace indicator.
   print('PI:', math.pi)  # use it


   # import the stdlib random module, but only make one of its objects
   # accessible
   from random import randrange
   
   # randrange is now part of the main namespace so we do not need a
   # random. qualifier to access it.
   # NEVER do this without thinking because you might overwrite your own
   # identifiers!
   print('A random number:', randrange(100))
   
   import numpy as np  # import the numpy extension package under the name np
   
   # The objects defined by numpy are now in a namespace called np.
   print("Numpy's pi", np.pi)
   
   
   # import the math and numpy modules, but make only one object from each
   # available under a custom name
   # As a beginner, DO NOT EVER DO THIS! It is just confusing.
   from math import pi as pi1
   from numpy import pi as pi2
   
   print("Let's compare some pis:", pi1, pi2)
   print('But which is which?')

   
Built-in Datatypes and Things You can do with them
--------------------------------------------------

Number Types
............

``int`` and ``float`` objects support basic arithmetic operations as we have
seen.

Container Types
...............

These are datatypes that contain other objects. Essentially all built-in types
that are not numbers fall into this category although different types have
restrictions on their content (*e.g.*, a ``string`` can only hold characters)
and on the way this content can be accessed.

All container types can be used with these built-in functions and operators to
investigate their content:

.. code:: python3

   len(c)  # how many items are in the container
   all(c)  # return True if all items evaluate to true, False otherwise
   any(c)  # return True if any item evaluates to true, False otherwise
   
   item in c   # membership test; returns True if the object item exists in c
   item not in c  # opposite of above
   
   sorted(c)   # generate a sorted ``list`` from the container items
   min(c), max(c)   # retrieve the smallest and the largest item, respectively
   
   # only if the items in the container support addition in the arithmetic sense
   sum(c)  # the sum of all items in the container
   
Container types can be used in ``for`` loops to retrieve their elements one by
one using this simple, general pattern:

.. code:: python3

   for item in container:
       # do something with the item here
       pass
       
There are two built-in functions, ``enumerate()`` and ``zip()``, that return
specialized iterators over container items, which can also be used in ``for``
loops:

.. code:: python3
   
   # enumerate returns an iterator over (index, item) tuples.
   # This iterator can be used in a for loop like this:
   for index, item in enumerate(container):
       # do something with index and item here
       pass
   # if you don't want the index values to start at 0, you can specify a
   # different start value as the second argument to enumerate
   for index, item in enumerate(container, 1):
       # 1-based indexing
       pass
           
   # zip returns an iterator over tuples of zipped elements of all containers
   # passed to it, i.e., something like this
   # (item1_container1, item1_container2, ...), (item2_container1, ...), ...
   # The iterator returns as many tuples as there are elements in the
   # shortest container.
   # In a for loop it can be used like this:
   for container1_item, container2_item in zip(container1, container2):
       # do something with the zipped items here
       pass

**Ordered** containers (strings, lists, tuples, ranges), also called
*sequences*, support all general container operations above, but, in addition,
offer:

.. code:: python3

   c.index(item)  # return position of the first occurence of item in c
   c.count(item)  # return the number of times item occurs in c
   
   # return an iterator over the elements of the container in reversed order
   reversed(c)  # use e.g. in a for loop
   
   # concatenation (NOT available for ranges)
   c1 + c2  # concatenation of containers of same type
   c * n    # generate a new container by concatenating it n times
   
They also support *indexing* and *slicing*:

.. code:: python3

   >>> txt = "Let's try indexing and slicing with this ordered container"
   
   # indexing
   >>> txt[0]  # positions in Python sequences are zero-based
   'L'
   >>> txt[4]
   's'
   >>> txt[-1] # the last element
   'r'
   >>> txt[-2] # the second last element
   'e'
   >>> len(txt)
   58
   >>> txt[58]  # the last element in the string is at position 57!!
   Traceback (most recent call last):
     File "<pyshell#26>", line 1, in <module>
       txt[58]
   IndexError: string index out of range
   
   # slicing
   >>> txt[1:3]  # subsequence from pos 1 up to, but not including pos 3
   'et'
   >>> txt[:3]  # if the start is at 0, it can be omitted
   'Let'
   >>> txt[53:] # get end of sequence starting from position 53
   'ainer'
   >>> txt[:-1] # get subsequence up to, but not including last element
   "Let's try indexing and slicing with this ordered containe"
   >>> txt[:]   # get a copy of the whole sequence
   "Let's try indexing and slicing with this ordered container"
   # slicing with a step size
   >>> txt[1:27:3] # subsequence from every third element in indicated range
   'esriena i'
   >>> txt[::3] # every third element of the whole sequence
   "L't di dli ttsrr nir"
   >>> txt[::-1] # the whole sequence backwards
   "reniatnoc deredro siht htiw gnicils dna gnixedni yrt s'teL"
   >>> txt[3:1:-1] # subsequence from pos 3 down to, but not including pos 1
   "'t"

Individual container types define additional operations on their content in the
form of *methods*. Here's a list of some of the most commonly used ones:

.. _string:
   
Strings
,,,,,,,

For a given string ``s`` the following methods give ``True`` / ``False``
answers:

.. code:: python3

  s.startswith(s2)  # does s start with the substring s2?
  s.endswith(s2)    # does s end with the substring s2?
  s.isalpha()  # are all characters in the string letters? 
  s.isdigit()  # are all characters in the string digits?
  s.isalnum()  # are all characters in the string letters or digits?
  s.isspace()  # are all characters in the string whitespace characters?
  s.isupper()  # are all letter characters in the string in upper case?
  s.islower()  # are all letter characters in the string in lower case?
   
The following methods return a modified copy of ``s``:

.. code:: python3

  s.replace(s1, s2)  # replace occurences of substring s1 in s with s2
  s.strip()    # remove any whitespace characters from the ends of s
  s.strip(s1)  # remove any of the characters in s1 from the ends of s
  s.lstrip([s1])  # like s.strip with/without argument, but only from left end
  s.rstrip([s1])  # -"- from right end
  s.upper()    # convert letter characters to their upper case versions
  s.lower()    # convert letter characters to their lower case versions
  s.capitalize()  # 1st character to upper case, rest to lower case
  s.title()    # 1st character of every word to upper, rest to lower case
  s.swapcase() # turn lower into upper case and vice versa
   
These methods split ``s`` into a *sequence* of substrings:

.. code:: python3

  s.split()       # split s on whitespace; => list of non-whitespace substrings
  s.split(sep)      # split s on sep; => list of in-between substrings
  s.partition(sep)  # split s on sep; => 3-element tuple of (head, sep, tail)
  
.. _join method of strings:

This method joins the string elements of the provided *container* using ``s``
as glue:

.. code:: python3

  s.join(sequence_of_strings)  # e.g., ', '.join(['A', 'B', 'C']) => 'A, B, C'
  
.. _list:

Lists
,,,,,

.. code:: python3

  # the following methods modify an existing list l
  # by adding, removing or shuffling elements
  # IMPORTANT: these methods do NOT return the result of their operation, but
  # the special object None
  l.append(x)       # append object x to the end of l
  l.extend(seq)     # append all elements of sequence seq to l
  l.insert(pos, x)  # insert object x into l at (the zero-based) position pos
  l.remove(x)       # remove first occurence of object x from l
  l.sort()          # sort l in place
  l.reverse()       # reverse l in place

  # other in-place operations that can be done on a list l are
  # slice assignment and slice deletion. 
  l[1:3] = seq     # replace elements 1 and 2 of l with the elements of seq
  del l[-3:]       # delete the last three elemments from l
  
  # the pop() method removes an element from a list AND returns it
  l.pop()      # remove the last element from l and return it
  l.pop(pos)   # remove the element at position pos and return it
  
.. _tuple:

Tuples
,,,,,,

Although *tuples* are like *lists* in that they can store any number of
elements of any type, they are also **immutable** and, thus, do not provide
any methods to manipulate their content.

.. _range:

Ranges
,,,,,,

A *range* is an evenly spaced sequence of integer numbers that is never stored
in memory as a whole. Instead a *range* object only stores the **recipe** to
generate its numbers and returns them on demand.

*Ranges* are created using the built-in ``range()`` function:

.. code:: python3

   # range() works similar to slicing
   
   # range with just a stop argument gives a range from 0 up to (but not
   # including) stop (i.e., a range of stop-many numbers 
   r = range(10)  # numbers 0,1,2,3,4,5,6,7,8,9
   
   # with two arguments (start, stop) it gives a range from start up to (but
   # not including) stop
   r = range(2,12)   # numbers 2,3,4,5,6,7,8,9,10,11
   
   # with three arguments (start, stop, step) it gives a range including start,
   # then every stepth number below stop
   r = range(2,12,2)   # numbers 2,4,6,8,10
   
   # with start > stop and step < 0, a range representing a decreasing series
   # of numbers is created. As always stop is NOT part of this series.
   r = range(10,0,-1)  # numbers 10,9,8,7,6,5,4,3,2,1
   
The ``range()`` function creates a ``range`` object. To retrieve actual numbers
from that object, you can:

- use it in a ``for`` loop, *e.g.*:

  .. code:: python3
  
     for n in range(10):
         print(n)
         
- use indexing to retrieve a specific number:

  .. code:: python3
     
     r = range(128, 32768)
     x = r[3]
     y = r[-5]
     
- turn the *range* or *slices* of it into a concrete sequence, *e.g.*:

  .. code:: python3
  
     r = range(32768)
     l = list(r)        # turn the whole range into a list of integers
     t = tuple(r[::2])  # create a tuple from every second number in the range
     
  Note that slicing a *range* gives a new (sub-) ``range`` object.

Like *tuples*, *ranges* are **immutable** once they have been created and don't
offer any methods to manipulate their content. Instead, a ``range`` object has
three *attributes* that let you predict the numbers you can get from it:

.. code:: python3

  r.start    # the first number contained in range r
  r.stop     # the first number not contained in range r anymore
  r.step     # the spacing between consecutive numbers in range r
  
.. _set:

Sets
,,,,

A set is an unordered collection of unique elements (like a mathematical set).
It is **mutable** and provides methods for adding and removing elements.

.. code:: python3

  # The following methods change the content of a set s.
  # They do NOT return the result of their operations, but the None object.
  s.add(x)       # add an object x to s; if x is already part of s, do nothing
  s.discard(x)   # remove object x from s; if x is not in s, do nothing
  s.remove(x)    # like discard(), but if x is not in s, raise a *KeyError*
  s.update(s2)   # add the content of set s2 to s; ignore elements already in s
  
Sets also offer a number of operations that correspond directly to operations
you could perform with mathematical sets:

.. code:: python3

  # Examples of set operations
  pets = {'dog', 'hamster', 'tortoise', 'goldfish'}
  mammals = {'mouse', 'dog', 'pig', 'rat', 'gorilla', 'hamster'}
  
  animals = pets | mammals                    # union
  pets_that_are_mammals = pets & mammals      # intersection
  pets_that_are_not_mammals = pets - mammals  # difference
  mammals_that_are_not_pets = mammals - pets  # difference
  pets ^ mammals  # symmetric difference (set of items unique to one set)
  
.. _dict:
.. _dictionary:

Dictionaries
,,,,,,,,,,,,

.. code:: python3

  # Adding and accessing elements to a dictionary is usually NOT done through
  # methods, but through indexing like for *lists*, where the keys represent
  # the index.
  d = {}  # create an empty dictionary
  d['Germany'] = 'Berlin'  # add Germany to a dictionary of capitals
  d['Germany']   # get values by their keys => 'Berlin'
  d['France']    # trying to access a non-existing key raises a *KeyError*
  d['France'] = 'Lyon'    # add the entry for France
  # reassigning to an existing key means the old value gets overwritten
  d['France'] = 'Paris'   # better
  del d['France']         # remove the entry for France
  d['France']             # yes, it is gone
  
  # The get() method lets you retrieve values without risking a KeyError.
  d.get('Italy', '?')  # access entry 'Italy'; return '?' if it doesn't exist
  
  # There is only one *method* that modifies the content
  # of an existing dictionary d and does NOT return the result of the
  # operation, but the None object instead.
  d.update(d2)  # add key/value pairs found in d2 to d
  # if any d2 keys exist in d, their value in d2 will overwrite the value in d
  
  # These methods remove an element from d AND return it:
  d.pop(key)  # remove the element stored under key from d and return its value
  d.popitem(key, value)  # remove a key/value pair from d; return it as a tuple
  
  # These methods help you retrieve some of the content from d.
  # They return special view objects that are most useful with for loops.
  d.values()  # return a view on the values of d
  d.items()   # return a view on the key/value pairs of d
  # use them like this:
  for value in d.values():
      # do something with the value here
  for key, value in d.items():
      # do something with key and value here
  # there is also a keys() method, but it's usually simpler to do this:
  for key in d:
      # do something with key here
      

String Formatting
-----------------

.. code:: python3

   format(16/6, '.2f')
   
   '16€ / 6 = {0:.2f}€'.format(16/6)
   

Files
-----

Use the built-in ``open()`` function to open text files from Python:

.. code:: python3

   # try to open a file named 'some_file' in the current working directory
   # for reading:
   f = open('some_file')    # raises FileNotFoundError if file doesn't exist
   f = open('some_file', 'r')  # same, but more explicit ('r' means read-only)
   f = open('path/to/some_file')  # open file in another folder (macOS, Linux)
   f = open(r'Documents\some_file')  # Windows (use backslash in paths)
   
   # try to open a file named 'some_file' for writing
   # IMPORTANT: will create the file if it does not exist, but if it exists,
   # **deletes** the old content without asking for confirmation (and there is
   # no undo!!)
   f = open('some_file', 'w') # 'w' for write-access; may raise PermissionError
   
   # try to open a file named 'some_file' for appending to it
   # => existing old content is preserved (although you will not be able to
   # read it in this mode)
   f = open('some_file', 'a') # 'a' for append; may raise PermissionError

   # try to create a file 'some_file' to be written to
   # => fails if the file exists already
   f = open('some_file', 'x') # 'x' for e*x*clusive creation
   
The ``open()`` function returns a ``file object`` (assigned to ``f`` in the
examples above) which has methods for reading from or writing to the file.

.. code:: python3

   f = open('some_file')
   content = f.read()  # Read the whole(!) content of the file into one string
   f.close()           # Close the file; ALWAYS do this when you are done
   
   f = open('some_file')
   f.read(80)          # read the first 80 characters from the file
   # file object methods always continue their operations from the last
   # position that was accessed (think of a magnetic tape)
   f.read()            # read the rest
   # if the last position was the end of the file further reading operations
   # return an empty string
   f.read()   # => ''; use f.seek(n) to rewind to the nth character in the file
   # no write access because we are in read-only mode
   f.write()  # raises io.UnsupportedOperation
   
Other options to read from a file:

- Use the ``readline()`` method to read the next line from a file
- Use the ``readlines()`` method to read all lines from a file.
  This method returns a *list* of *strings* (one per line).
  You can provide a number of characters to read, then when that number is
  reached or surpassed at the end of any line, no further lines will be read.
- Use the ``file object`` in a for loop to retrieve lines one by one, like in:

  .. code:: python3
  
     for line in f:
         if 'PASSWORD' in line:
             print(line)
             
Files opened in ``'w'``, ``'a'`` or ``x`` mode have file objects without read
methods, but with corresponding write methods instead:

.. code:: python3

   f.write('some text')   # write a string to a file
   f.writelines(seq_of_strings)   # write a sequence of strings to a file
   
Both of these methods will not add line breaks for you so you have to use the
newline character ``\n`` in your strings explicitly to insert them.

For write operations, in particular, it is crucial that you close the file
after you are done because without that your data may not actually get written
to the file, but only be scheduled for writing.

Because it is easy to forget closing files, Python offers this idiom for
opening a file for use in only a specific block of code. When execution leaves
the block, the file will be closed automatically.

.. code:: python3

   with open('some_file', 'w') as f:
       # within this block we have write access to 'some_file'
       # this would have worked with 'r' as well
       f.write('some text')
       
   # once we get here, Python will have closed the file for us
   f.write('more text')  # will raise ValueError because of closed file

Use this preferentially to avoid problems!
  
