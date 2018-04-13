Installation of the spyder IDE
==============================

Open a console window
---------------------

The easiest way (working under any version of Windows) is to:

- press ``Win`` + ``R`` on the keyboard
- type ``cmd`` into the *Run dialog* input field
- press ``Enter`` or click the **OK** button


Check that Python got set up correctly
--------------------------------------

Type **exactly** the following into the console window and press ``Enter``::

  py -3 -V
  
This should report your installed version of Python3. If that works, Python3 is
installed correctly on your system along with the *py* Python launcher.

.. admonition:: The Python launcher

   The Python launcher is a small program available only for Python
   installations on Windows (*i.e.*, not on macOS or Linux) that lets you start
   Python and even different versions of it easily from within the console.
   
   The launcher is invoked with the command ``py``. The ``-3`` in the command
   above tells the program to launch the latest version of Python3 that it can
   find on your system. All options following this so-called Python version
   identifier switch are passed on to Python. In our example, the ``-V`` option
   instructs Python to report only its version, then quit again.
   

Update *pip*
------------

*pip* is the Python package manager, which allows you to install third-party
extension packages for your installation of Python. It comes bundled with
Python3, but the version you obtained with your download may not be up-to-date.
To ensure you are working with the latest *pip* version, use this command in
the console::

  py -3 -m pip install pip --update
  
This invokes Python3 as before, but this time instructs it to use its own *pip*
module (``-m pip``) to update itself (``install pip --update``).

.. admonition:: Installation rights

   If you opted for an *installation for all users* when you installed Python,
   then updating *pip* will require Admin privileges and you will get a
   ``PermissionError`` with the above command.
   
   In that case, you will have to run the console window as Admin. With the
   current window open, you can just right-click the *console* icon on the
   task bar, right-click *Command Prompt* in the context menu, then select
   (left-click) *Run as administrator*, as shown in the screenshot below.
   
   .. image:: source/cmd_as_admin.png


Install spyder
--------------

Installing spyder for Windows is currently done in a somewhat unusual way and
you may want to install it in a location that is separate from Python itself.
This way, if you are unhappy with *spyder*, deleting it is just a matter of
deleting a single directory in your file system.
For installing extension packages like *spyder* separately from Python itself,
Python offers the concept of *virtual environments*.

Generate a virtual environment for spyder
.........................................

From a regular console window (not one running with Admin privileges), run::

  py -3 -m venv spyder_env
  
This will create a virtual environment named *spyder_env* (you are free to
choose a different name, of course). As far as we are concerned right now, this
is just a directory created inside the currently active working directory (the
one displayed in front of every command you type in the console). However,
inside that directory there is a script that, when executed, automagically
makes Python use the extension packages stored inside of it.
This script is called ``activate`` and can be run by typing::

  spyder_env\Scripts\activate
  
Of course, if you gave your virtual environment a different name, you will need
to replace ``spyder_env`` with the name of your environment.

To deactivate the environment (and all its extension packages) again, just
run::

  deactivate
  
, but leave it activated for now to install *spyder* into it.

Get spyder
..........

When *pip* is used with a virtual environment activated, it will install new
packages into this environment automatically, *i.e.*, everything you
*pip*-install while a virtual environment is active, will only be accessible to
Python when that specific environment is active. So all we have to do to
install *spyder* into the current environment is to run::

  py -m pip install spyder


.. Warning::
   
   Don't use the ``-3`` version identifier switch from the previous sections
   when inside a virtual environment. Without it the launcher will detect that
   you have a virtual environment activated, but the switch will make it ignore
   the environment and use your regular Python3 with just your regularly
   installed extensions.
   
This command will take a while to complete because it installs *spyder* and all
packages that *spyder* needs in turn.

Once it completes you can start *spyder* simply by running::

  spyder3
  
However, this would require you to open a console window and activate the
virtual environment every time you want to use the IDE, so in the next step we
are going to make *spyder* more easily accessible.

Creating a spyder shortcut
..........................

- Open *Windows Explorer* and navigate to the folder containing your virtual
  environment.
- Open the subfolder *Scripts* and look for a file called ``spyder3.exe``.
- Drag the file to a more easily accessible location, *e.g.*, the desktop, but
  keep ``Ctrl`` (or ``Strg`` on a German keyboard) **and** ``Shift`` pressed,
  while dropping the file in the new location to create a *link* instead of
  moving the file. If you move the file accidentally instead, move it back and
  try again.
  
You should now be able to start *spyder* just by double-clicking on the link!


