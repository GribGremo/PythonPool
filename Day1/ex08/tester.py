from ft_filter import ft_filter 

def what(x) -> bool:
    if x % 2 == 0:
        return True
    else :
        return False

def main() :
    test = [1, 2, 3, 4, 5, 6]
    bcn = ft_filter(what,test)
    for i in bcn:
        print (i)

if __name__ == "__main__":
    main()

#NOTIONS
#for permet de capter directement l'exception StopIteration a l'inverse de while attention
#for permet egalement la recuperation de l'iterateur a la base