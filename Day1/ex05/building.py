"""This is module documentation"""
import sys

def count(char, ct_lower, ct_upper, ct_punct, ct_digit, ct_space) -> None:
    if (char.islower()):
        ct_lower += 1
    elif(char.isupper()):
        ct_upper += 1
    elif(char.ispunct()):
        ct_punct += 1
    elif(char.isdigit()):
        ct_digit += 1
    elif(char.isspace()):
        ct_space += 1

def main() -> int:
    """Return nomber of lowecase, uppercase, punctuation characters digits and spaces in a string """
    # print(__doc__)
    # print(main.__doc__)

    ct_lower = 0
    ct_upper = 0
    ct_punct = 0
    ct_digit = 0
    ct_space = 0

    print(type(sys.argv[1]))
    assert len(sys.argv) == 2, "Invalid number of arguments"
    lst_str = list(sys.argv[1])
    print(lst_str)
    map(count,lst_str, ct_lower, ct_upper, ct_punct,ct_digit, ct_space)
    print(f"The text contains 171 characters: {ct_upper} upper letters {ct_lower} lower letters {ct_punct} punctuation marks {ct_space} spaces {ct_digit} digits")
    return 1

if __name__ == "__main__":
    main()

#https://www.pythoniste.fr/python/quest-ce-quun-generateur-en-python/
#https://www.geeksforgeeks.org/python/python-map-function/