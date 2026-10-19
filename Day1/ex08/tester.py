from ft_filter import ft_filter


def what(x) -> bool:
    """Return boolean according to odd/even number"""
    if x % 2 == 0:
        return True
    else:
        return False


def main():
    """Main function to test ft_filter"""
    test = [1, 2, 3, 4, 5, 6]
    print("~~~~~~~~~ TEST FT_FILTER~~~~~~~~~")
    print("Test 1:")
    bcn = ft_filter(what, test)
    print("Test next")
    print(next(bcn))
    print("Test loop since newsetpoint(4 in this case)")
    for i in bcn:
        print(i)
    print("Test 2:")
    print(list(ft_filter(None, [0, 1, 2, False, True, "", "hello"])))
    print(ft_filter.__doc__);

    print("~~~~~~~~~ TEST FILTER~~~~~~~~~")
    print("Test 1:")
    bcn = filter(what, test)
    print("Test next")
    print(next(bcn))
    print("Test loop since newsetpoint(4 in this case)")
    for i in bcn:
        print(i)
    print("Test 2:")
    print(list(filter(None, [0, 1, 2, False, True, "", "hello"])))
    print(filter.__doc__);

    print("~~~~~~~~~TEST WHILE FT-FILTER~~~~~~~~~")
    bcn = ft_filter(what, test)
    while (True):
        try:
            print("Pre-next")
            value = next(bcn)
            print(value)
            print("Post-next")
        except StopIteration:
            print("StopIteration caught: End of loop")
            break
        
    print("~~~~~~~~~TEST WHILE FT-FILTER~~~~~~~~~")
    bcn = filter(what, test)
    while (True):
        try:
            print("Pre-next")
            value = next(bcn)
            print(value)
            print("Post-next")
        except StopIteration:
            print("StopIteration caught: End of loop")
            break


if __name__ == "__main__":
    main()

# NOTIONS
# for permet de capter directement l'exception StopIteration
# a l'inverse de while attention
# for permet egalement la recuperation de l'iterateur a la base
