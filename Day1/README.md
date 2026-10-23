*Python Pool Day1 at 42 Angouleme Campus by the student sylabbe*

# Day1

>This is the first steps on learning python


## Overview

>In this you will see different notions of Python:
* iterables
* built-in
* strings format
* date
* functions
* NULL
* AssertionError
* flake
* main
* __doc__
* sys.argv
* list comprehension
* expression generator
* lambdas
* yield
* packets


## Installation/uninstall

> Get updated versions of python3, pip. Or you might have some unpleasant surprise with packet installation

## Utils
> If flake8 is not installable on you PC, your must use a .venv.

### Creation of virtual environment for python
Create a copy of your python environment
* ```python3 -m venv .venv```
Print python version
* ```python3 --version```
Launch your virtual environment
* ```source .venv/bin/activate```
Indicate the path of the actual python environment
* ```which python``` 
Exit python environment(not erased)
* ```deactivate```

### Flake8
Launch flake8 without .venv
* ```flake8 . --exclude=.venv```

[flake8]
exclude = .venv
