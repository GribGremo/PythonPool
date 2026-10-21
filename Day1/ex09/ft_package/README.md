*This python package is made as an exercise purpose on 42 Angouleme Campus by the student sylabbe*

# ft_package

>This is an exercise of school 42 python pool Day1/ex09, his purpose is to learn how to create a python package.


## Overview

>This package contain a simple function count-in-list, receive an iterable and a comparator, for each occurence of the comparator in the iterable, increment a counter and return it at the end.

## Requirements

Python 3.10 or above

## Installation/uninstall

Install the package using pip
* ``` pip install ft_package/dist/ft_package-0.0.1.tar.gz ```
or
* ``` pip install ft_package/dist/ft_package-0.0.1-py3-none-any.whl ```
or (from Pypi)
* ``` pip install ft_package ```

Uninstall
* ``` pip uninstall ft_package ```

## Utils

Print package information
* ``` pip show -v ft_package ```

Print list of packages
* ``` pip list ```

## Publish
Install twine
* ``` python -m pip install twine ```
Upload package
* ``` python -m twine upload dist/* ```

## Creation
### Files required
* __init__.py
* LICENCE
* pyproject.toml
* README.md
* Any other files you want to be included in your package

### Build

Install build module for python(if needed)
* ``` python3 -m pip install --upgrade build ```
Build the package(creating dist et egginfo)
* ``` python3 -m build ```

## Informations
### Global files
* LICENSE: To declare rights about that package
* .toml: contain all datas about that package
* __init__.py: originally define a package to python, dispatch all modules

### .egg-info
* PKG-INFO : informations about package(name, author,...)
* SOURCES.txt : File being part of package
* top_level.txt : indicate pytthon packages/modules at superior level of tree
* dependency_links.txt : informations about dependancies links

### dist
* .tar.gz: contain source code, metadata, compiled code if needed
* .wheel: is a pre-package ready to be installed on python

## Sources
* https://packaging.python.org/en/latest/tutorials/packaging-projects/