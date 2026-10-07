from ft_filter import ft_filter 

def what(x) -> bool:
    """Return boolean according to odd/even number"""
    if x % 2 == 0:
        return True
    else :
        return False

def main() :
    """Main function to test ft_filter"""
    test = [1, 2, 3, 4, 5, 6]
    print("~~~~~~~~~ TEST FT_FILTER~~~~~~~~~")
    print("Test 1:")
    bcn = ft_filter(what,test)
    for i in bcn:
        print (i)
    print("Test 2:")
    print(list(ft_filter(None, [0, 1, 2, False, True, "", "hello"])))

    print("~~~~~~~~~ TEST FILTER~~~~~~~~~")
    print("Test 1:")
    bcn = filter(what,test)
    for i in bcn:
        print (i)
    print("Test 2:")
    print(list(filter(None, [0, 1, 2, False, True, "", "hello"])))



if __name__ == "__main__":
    main()

#NOTIONS
#for permet de capter directement l'exception StopIteration a l'inverse de while attention
#for permet egalement la recuperation de l'iterateur a la base