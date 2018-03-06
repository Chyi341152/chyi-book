# Modules and Packages : Live and Let Die

*Tutorial Presentation at PyCon'2015.  April 9, 2015.  Montreal.*

*David Beazley (@dabeaz), http://www.dabeaz.com*

This tutorial assumes the use of Python 3.4 or newer.  Certain examples
in sections 8 and 9 require the use of Python 3.5. 

The official website for this tutorial is http://www.dabeaz.com/modulepackage/index.html

## Part 1 - Basic Knowledge

```text
Any Python source file is a module
When a module is imported, all of the statements in the module execute one after another until the end of the file is reached

Naming Conventions:
    It is standard practice for package and module names to be concise and lowercase 
    Use a leading underscore for modules that are meant to be private or internal 
    Don't use names that match common standard library modules (confusing)

Module Search Path:
    >>> import sys 
    >>> sys.path 
    >>> sys.path.append("/project/foo/myfiles")

Module Cache 
    Modules only get loaded once 

Module Reloading 
    You can force-reload a module, but you're never supposed to do it 
    >>> from importlib import reload
    >>> reload(spam)
    
Modules vs. Packages 
    Modules are easy -- a single file 
    Packages are hard -- multiple related files 
    
    Don't use implicit relative imports in packages [It "work" in Python 2, but not Python 3]
    
    Implicit Relative 隐式 
    Absoluute Imports 
    Explicit Relative Imports 显示相对, acceptable to absolute imports, especially when 
    
__init__.py

Controlling Exports 
    Each submodule should define __all__ , Controls behavior of "from module import *"

Main Modules
    python -m module # runs a module as a main program  

sys.path
    Directory name, Traversed start-to-end looking for imports 
    .zip files added to sys.path work as if they were normal directors 
    .egg files are actually just directories or .zip files with extra metadata 
    
    python3 -vv verbose output 
    
    sys.path is constructed form three parts {sys.prefix, PYTHONPATH, site.py}
    python3 -S # -S skips site.py initialization 
    sys.prefix: base location of Python installation 
    sys.exec_prefix: is location of compiled binaries (C
    
    Paths in PYTHONPATH go first! 
    site.py adds third-party module directories 
    
venv site-packages
    # Include system site-packages 
    $ python3 -m venv --system-site-packages mypython 
    
.pth files
    All directories .pth file exist are added to sys.path 
    .pth files mainly used by package managers to install packages in additional directories 
    
Package Managers 
    

```


`basic_package/` : A very simple package consisting of multiple files.

## Part 2 - Packages

`package_assembly/` : An example of assembling a package from submodules
by exporting symbols in `__init__.py` files.

`decorator_assembly/`: Assemble a package from submodules using a special
`@export` decortor.

## Part 3 - __main__

`main_wrapper` : An example of writing a module that wraps around a script 
using the `-m` option.

## Part 4 - sys.path

No code samples for this part.

## Part 5 - Namespace Packages

`namespace_package` : A simple namespace package example.

`telly` : A package that uses namespace packages to allow for user-extensible submodules.

## Part 6 - The Module
```text
Module Objects:
    Module Attributes
        __name__        # Module name 
        __file__        # Associated source file (if any)
        __doc__         # Doc string 
        __path__        # Package path 
        __package__     # Package name 
        __spec__        # Module spec 
       

```

`mini_import` : A minimalistic implementation of the `import` statement.

`subpackage_cycle` : A package where submodules import each other in a cycle.

`import_patch` : An example of patching the builtin `__import__()` function.

## Part 7 - The Module Reloaded
```text
>>> import spam
>>> from importlib import reload
>>> reload(spam)

Reloading in a nutshell
>>> import spam 
>>> code = open(spam.__file__, 'rb').read()
exec(code, spam.__dict__)



```
`reload_instances` : A class that detects reloading and updates instances.

`reload_func` : A context manager that allows reloadable functions to be declared.

## Part 8 - Import Hooks

`trial_import` : A module that tests for another module with `import`

`check_import` : A module that tests for another module using module specs.

`lazy_import` : A module that only executes when accessed for the first time.

`watcher` : A simple import hook.

`autoinstall` : An import hook that automatically installs missing modules.

`redisimport` : An import hook that loads modules from Redis.

## Part 9 - Path Hooks

`webhook` : An import hook that allows URLs to be placed on `sys.path`.
