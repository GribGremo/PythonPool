import sys
import string


def main() -> int:
    """Split words and verify theyre length,
    if they are superior to the integer send as argument,
    the word will be print"""

    assert len(sys.argv) == 3, "Invalid number of arguments"
    assert type(sys.argv[1]) is str, "First argument should be a string"

    arg1 = sys.argv[1]
    try:
        arg2 = int(sys.argv[2])
    except ValueError:
        print("Second argument should be an integer")
        exit()
    # check_str = lambda c: c.isprintable() and c not in string.punctuation
    assert all(
        lambda c: c.isprintable() and c not in string.punctuation
        for c in arg1
        ), "Invalid characters in string"

    # check_len = lambda w: len(w) > arg2
    lst_str = arg1.split()
    cut_words = [
        w for w in lst_str
        if len(w) > arg2]
    print(cut_words)


if __name__ == "__main__":
    main()

# NOTIONS
# Il semblerait que pour les entrees d'un programme on utilise
# plutot argparse que assert hors ici il n'est pas autorise

# https://www.w3schools.com/python/python_lists_comprehension.asp
