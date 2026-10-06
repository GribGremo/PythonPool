**This python package is made as an exercise purpose on 42 Angouleme Campus by the student sylabbe**



python3 -m pip install --upgrade build
Install "build" tool to python
python3 -m build
Build the package(creating dist et egginfo)


LICENSE: To declare rights about that package
.toml: contain all datas about that package
__init__.py: originally define a package to python, dispatch all modules

.egg-info
PKG-INFO : informations about package(name, author,...)
SOURCES.txt : File being part of package
top_level.txt → indique notamment les modules/packages Python présents au niveau supérieur.
dependency_links.txt → informations sur d'éventuels liens de dépendances.

dist
.tar.gz: contain source code, metadata, compiled code if needed
.wheel: is a pre-package ready to be installed on python

https://packaging.python.org/en/latest/tutorials/packaging-projects/