"""This file identify package, and display our modules as we want,
If we import modules in it, no need to specify later(be careful heavy modules),
 you can also make lazy import using getattr()"""

from .count_in_list import count_in_list


print("ft_package has been loaded")

# Here you can import from different files, the point "." is here
# to show from "this" current package

# flake8 error import
# import in __init__.py, trigger a flake8 error considering
# you import and not use it, that's the whole point of init file
# import module(s) that will be used later by another file
# i prefer to import directly in init you don't have to target
# your module when importing later, for light module it's simpler