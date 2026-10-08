def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    # print(ft_filter.__doc__)
    for i in iterable:
        if function is None:
            if i:
                yield i
        elif function(i):
            yield i


# https://packaging.python.org/en/latest/tutorials/packaging-projects/
# https://realpython.com/ref/builtin-functions/filter/
# https://courspython.com/classes-et-objets.html

# This function will filter using a function and an iterable.
# For each element the function will be apply and return a boolean.
# It uses yield tranforming this function in a generator and return
# an object generator, applying next() to this object it will produce
# a value and stop his execution to this point,
# when no more yield is present it raises StopIteration
