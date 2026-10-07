"""This file identify package, and can be used to display our modules as we want, if we import modules in it, no need to specify later(be careful heavy modules), you can also make lazy import using getattr()"""

print("ft_package has been loaded")

from .count_in_list import count_in_list

#Here you can import from different files, the point "." is here to show from "this" current package