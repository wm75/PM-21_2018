Python 3 cheat sheet - Beginner's level
=======================================

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

Integer number objects can be generated from other types using the ``int``
function, *e.g.* :

.. code:: python3

   >>> int("15")    # integer number from string
   15
   
   >>> int("15.0")  # string MUST represent an integer
   Traceback (most recent call last):
     File "<pyshell#40>", line 1, in <module>
       int("15.0")
   ValueError: invalid literal for int() with base 10: '15.0'
   
   >>> int(15.3)    # integer from floating point number (decimal digits get truncated)
   15
   

Floating point number objects can be generated from other types using the
``float`` function:

.. code:: python3

   >>> float("3.1415")    # float object from string
   3.1415
   
   >>> float("31415e-4")  # float object from string in scientific format)
   3.1415
   
   >>> float(15)          # float object from integer
   15.0
   
Lists, tuples and sets can be interconverted or generated from other sequence
types using correspondingly named functions:

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
   
Dictionaries can be generated from sequences of pairs of items:

.. code:: python3

   >>> dict([("a", 1), ("b", 2), ("c", 3)])  # from a list of 2-element tuples
   {'a': 1, 'b': 2, 'c': 3}
   
To convert a dictionary to a list, tuple or set, you have to decide if you want
just the keys, the values, or both converted:

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


Importing code from modules
---------------------------

.. code:: python3

   import math   # import the Python math module that is part of the stdlib
   
   # All objects defined in math can now be accessed through their
   # identifiers preceeded with math. namespace indicator.
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
   
   # built-in functions that accept a container and return an iterator
   # for use, e.g., in a for loop
   
   # return an iterator over (index, item) tuples
   enumerate(container1, container2, ...)
   # return an iterator over tuples of zipped elements of all containers, i.e.,
   # (item1_container1, item1_container2, ...), (item2_container1, ...), ...

**Ordered** containers (strings, lists, tuples, ranges) also support these
additional operations:

.. code:: python3

   c.index(item)  # return position of the first occurence of item in c
   c.count(item)  # return the number of times item occurs in c
   
   # return an iterator over the elements of the container in reversed order
   reversed(c)
   
   # concatenation
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

.. _string:
   
Strings
,,,,,,,


.. _list:

Lists
,,,,,

.. _tuple:

Tuples
,,,,,,

.. _range:

Ranges
,,,,,,

.. _set:

Sets
,,,,

.. _dictionary:

Dictionaries
,,,,,,,,,,,,

