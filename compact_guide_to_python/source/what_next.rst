What's next?
============

Generator expressions and functions
-----------------------------------

The problem:
............

.. code:: python3

   # List comprehensions are great ...
   odd_numbers = [n for n in range(10) if n % 2]   # => [1, 3, 5, 7, 9]
   
   # but may consume LOTS of memory (don't try this at home):
   # many_odd_numbers = [n for n in range(100000000) if n % 2]
   
The solution - generator expressions:
.....................................

Just replace the square brackets with parentheses and things inside will be
evaluated lazily (*i.e.*, elements will get produced only on demand):

.. code:: python3

   # the following is safe and returns the equivalent of range(0, 100000000, 2)
   odd_number_generator = (n for n in range(100000000) if n % 2)
   type(odd_number_generator)    # => <class 'generator'>
   
Generators are a great solution in filtering and accumulating applications, in
which you never need all elements in memory at the same time, *e.g.*:

.. code:: python3

   # sum of all numbers below 10**9 that are not multiples of 2, 3 or 5
   # takes a while, but will complete eventually (without any memory issues)

   sum(n for n in range(10**9) if n % 2 and n % 3 and n % 5)

   # as you can see, the parentheses around the generator expression can be
   # omitted if this does not create syntactical ambiguity
   
   # It is even possible to chain generators together as in:
   number_range = range(10**9)
   exclude_multiples_of_2 = (n for n in number_range if n % 2)
   exclude_multiples_of_3 = (n for n in exclude_multiples_of_2 if n % 3)
   exclude_multiples_of_5 = (n for n in exclude_multiples_of_3 if n % 5)
   # now do all the work
   sum(exclude_multiples_of_5)
   
Generator *functions* offer even more flexibility than generator expressions.
The hallmark of generator functions is that they use ``yield`` instead of
``return`` and remember their state across calls.

For more on generators and iteration over them see for example:
https://nedbatchelder.com/text/iter.html


Real object-oriented programming
--------------------------------

- Learn to write your own classes
- Understand that many, many things in Python are really classes or instances
  thereof


Python dunder methods and protocols
-----------------------------------

The behavior of Python classes can be modified through dunder methods and
things like the ``iterator protocol`` and the ``contextmanager protocol``
completely depend on them. The ``iterator protocol`` should be relatively easy
to understand, the ``contextmanager protocol`` is somewhat harder.


Write better command line parsers with the argparse module
----------------------------------------------------------

``argparse`` is a stdlib module -> learn how to use it


Non-Python-specific tools
-------------------------

- Learn Markdown and/or reStructuredText (use docutils rst2html to build html)
- Continue practicing with git and github


Try to solve real-world problems through programming
----------------------------------------------------

This is by far the best way to learn!


Continue learning and never be afraid
-------------------------------------

- Programming is never really rocket science, it just takes persistence.
- Read about programming as often as possible (books, artciles, etc.)
- Other sources of information: StackOverflow,
  Newsgroups: gmane.comp.python.general, gmane.comp.python.tutor,
  Newsletter: Python Weekly
- For the ambitious people: in the long run, try to learn a second language
  (Javascript, C, Java, Scala, Go, ??)
