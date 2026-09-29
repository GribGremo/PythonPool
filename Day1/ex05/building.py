"""PythonPool/Day1/Ex05"""
import sys
import string

#Is string allowed

def main() -> int:
    """Return nomber of lowercase, uppercase, punctuation characters, digits and spaces in a string """
    # print(__doc__)
    # print(main.__doc__)

    assert len(sys.argv) == 2, "Invalid number of arguments"

    ct_lower = sum(c.islower() for c in sys.argv[1])
    ct_upper = sum(c.isupper() for c in sys.argv[1])
    ct_digit = sum(c.isdigit() for c in sys.argv[1])
    ct_space = sum(c.isspace() for c in sys.argv[1])
    ct_punct = sum(c in string.punctuation for c in sys.argv[1])

    print(f"The text contains {len(sys.argv[1])} characters: {ct_upper} upper letters {ct_lower} lower letters {ct_punct} punctuation marks {ct_space} spaces {ct_digit} digits")
    return 1

if __name__ == "__main__":
    main()

#https://www.pythoniste.fr/python/quest-ce-quun-generateur-en-python/
#https://www.geeksforgeeks.org/python/python-map-function/

