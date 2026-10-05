def ft_filter(function,iterable):
    #
    for i in iterable:
        if function is None:
            if i:
                yield i
        if function(i):
            yield i



#https://packaging.python.org/en/latest/tutorials/packaging-projects/
#https://realpython.com/ref/builtin-functions/filter/
#https://courspython.com/classes-et-objets.html