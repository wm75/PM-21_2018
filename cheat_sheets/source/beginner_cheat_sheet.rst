Python 3 cheat sheet - Beginner's level
=======================================

Arithmetics
-----------

.. code::

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
  
- ``"Hello World"`` or ``'Hello World'`` create the **string** *Hello World*
  (whether you use single or double quotes is up to you, but having the choice
  simplifies the creation of strings that themselves contain one of the
  quote types, e.g., ``'I said: "Hello World"'``)
  
- ``[1, 2, 3]`` creates a **list** of three integers (a comma after the last
  element is allowed, so ``[1, 2, 3,]`` is an equivalent literal);
  to create a list with just one element, you can use, *e.g.*, ``[1]`` or
  ``[1,]``; the literal for an empty list is ``[]``

- ``(1, 2, 3)`` or ``(1, 2, 3,)`` (trailing comma) creates a three-element
  **tuple**;
  to create a single-element tuple, the trailing comma is obligatory as in
  ``(1, )`` (because ``(1)`` just represents the integer 1 in parentheses);
  the literal for an empty tuple is ``()``
  
- ``{1, 2, 3}`` is a three-element **set** literal; like for list literals a
  comma after the last element is allowed; a single-element set can be written
  as ``{1}`` or ``{1, }``; there is no empty set literal (**!!** ``{}`` is
  used to denote an empty dictionary **!!**)

- ``{"a": 1, "b": 2, "c: 3"}`` represents a **dictionary** with three key/value
  pairs; again, a comma after the last element (*i.e.*, the last pair) is
  allowed; ``{}`` is the empty dictionary literal
  

Conversion between object types
-------------------------------

Integer number objects can be generated from other types using the ``int``
function, *e.g.* :

.. code::

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

.. code::

   >>> float("3.1415")    # float object from string
   3.1415
   
   >>> float("31415e-4")  # float object from string in scientific format)
   3.1415
   
   >>> float(15)          # float object from integer
   15.0
   
Lists, tuples and sets can be interconverted or generated from other sequence
types using correspondingly named functions:

.. code::

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

.. code::

   >>> dict([("a", 1), ("b", 2), ("c", 3)])  # from a list of 2-element tuples
   {'a': 1, 'b': 2, 'c': 3}
   
To convert a dictionary to a list, tuple or set, you have to decide if you want
just the keys, the values, or both converted:

.. code::

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

.. code::

   >>> x = 1.2 + 8*2

   >>> special_numbers = [2, 3, 3.1415, 12, 13, 42, 666, 1001]
   
The expression on the right side gets evaluated (to the float object ``17.2``
or a list object) and bound to the identifiers named ``x`` and
``special_numbers``, respectively. After that, these identifiers can be used
anywhere ``17.2`` or the list ``[2, 3, 3.1415, 12, 13, 42, 666, 1001]`` could
be used:

.. code::

   >>> x - 3
   14.2
   
   >>> y = x // 2  # calculate 17.2 // 2 and assign the result (8.0) to y
   
   >>> x = x * x   # calculate 17.2*17.2 and assign the result back to x
   
   >>> x = x - 3
   292.84
   
   >>> set(special_numbers)
   {2, 3.1415, 3, 1001, 42, 12, 13, 666}
   

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


Flow Control
------------

Repeated and/or conditional code execution is achieved through

- ``for`` and ``while`` loops, possibly with contained ``break`` and/or
  ``continue`` instructions
- ``if``/``elif``/``else`` constructs

Inside functions, flow control can also be achieved with ``return`` statements.



