ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


ft_list.append("World")

ft_tuple = ft_tuple[:1] + ("France",)
ft_set.remove("tutu!")

ft_set.add("Angouleme")

ft_dict["Hello"] = "42Angouleme"




#your code here
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)



#Expected output:
#$>python Hello.py | cat -e
#['Hello', 'World!']$
#('Hello', 'France!')$
#{'Hello', 'Paris!'}$
#{'Hello': '42Paris!'}$


#NOTIONS
# ':'  slice ( plage d'inclusion exclusion)
# ':5' inclus de debut a 5
# '5:' exclus de 5 a la fin
# '5:10' inclus de 5 a 10
# '5:10:2' inclus de 5 a 10 sur les intervalles de 2 (5 7 9)

#La virgule ici est la pour que python comprenne qu'il s'agit d'un tuple

#https://courspython.com/dictionnaire.html
#https://www.w3schools.com/PYTHON/python_ref_set.asp
#https://blog.stephane-robert.info/docs/developper/programmation/python/tuple/
#https://www.w3schools.com/Python/python_ref_list.asp
#https://www.w3schools.com/PYTHON/python_ref_set.asp