ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# List is mutable
# Basic, append add an element at the end of my list
ft_list.append("World")

# Tuple is not mutable
# I re-assignate a new tuple result of the concatenation of 2 tuples
# First one is a range of ft_tuple(start to 1)
# Second is a tuple litteral i create (comma to clarify it's a tuple)
ft_tuple = ft_tuple[:1] + ("France",)

# Set is mutable, his elements are not
# set does not ensure a specific order when printed,
# it hashes set's elements to access them faster,
# this is why Angouleme can be print first
ft_set.remove("tutu!")
ft_set.add("Angouleme")

# Dictionnary is mutable
# Key pair works just as C++
ft_dict["Hello"] = "42Angouleme"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# Expected output:
# $>python Hello.py | cat -e
# ['Hello', 'World!']$
# ('Hello', 'France!')$
# {'Hello', 'Paris!'}$
# {'Hello': '42Paris!'}$

# NOTIONS
# ':'  slice ( plage d'inclusion exclusion)
# ':5' inclus de debut a 5
# '5:' exclus de 5 a la fin
# '5:10' inclus de 5 a 10
# '5:10:2' inclus de 5 a 10 sur les intervalles de 2 (5 7 9)

# List is a collection which is ordered and changeable.
# Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable.
# Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed.
# No duplicate members.
# Dictionary is a collection which is ordered** and changeable.
# No duplicate members.

# https://courspython.com/dictionnaire.html
# https://www.w3schools.com/PYTHON/python_ref_set.asp
# https://blog.stephane-robert.info/docs/developper/programmation/python/tuple/
# https://www.w3schools.com/Python/python_ref_list.asp
# https://www.w3schools.com/PYTHON/python_ref_set.asp
# https://www.w3schools.com/python/python_dictionaries.asp
# https://www.w3schools.com/python/python_tuples.asp
