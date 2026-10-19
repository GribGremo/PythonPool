"""PythonPool/Day1/Ex05"""
import sys


def main() -> int:
    """Return nomber of lowercase, uppercase, punctuation characters,
      digits and spaces in a string """
    # print(__doc__)
    # print(main.__doc__)
    assert len(sys.argv) < 3, "Invalid number of arguments"

    punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    if len(sys.argv) == 1:
        entry = input("What is the text to count?\n")
    else:
        entry = sys.argv[1]

    ct_lower = sum(c.islower() for c in entry)
    ct_upper = sum(c.isupper() for c in entry)
    ct_digit = sum(c.isdigit() for c in entry)
    ct_space = sum(c.isspace() for c in entry)
    ct_punct = sum(c in punct for c in entry)

    print(f"The text contains "
          f"{len(entry)} characters: \n"
          f"{ct_upper} upper letters \n"
          f"{ct_lower} lower letters \n"
          f"{ct_punct} punctuation marks \n"
          f"{ct_space} spaces \n"
          f"{ct_digit} digits")
    return 1


if __name__ == "__main__":
    main()

# https://www.pythoniste.fr/python/quest-ce-quun-generateur-en-python/
# https://www.geeksforgeeks.org/python/python-map-function/
# https://www.expertpython.fr/lexique/input()

# python3 building.py '!"#$%&'\''()*+,-./:;<=>?@[\]^_`{|}~'
