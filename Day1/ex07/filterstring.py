"""PythonPool/Day1/Ex07"""
import sys


def main() -> int:
    """Split words and verify theyre length,
    if they are superior to the integer send as argument,
    the word will be print"""

    assert len(sys.argv) == 3, "Invalid number of arguments"

    punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    arg1 = sys.argv[1]
    try:
        arg2 = int(sys.argv[2])
    except ValueError:
        raise AssertionError("Second argument should be an integer")
    assert all(
        # charcheck(arg1)
        (lambda arg: [c.isprintable() and c not in punct for c in arg])(arg1)
        ), "Invalid characters in string"

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
# L'exercice est un peu illogique flake interdit d'assigner un
# lambda, et ces lambdas finissent par etre creer puis utiliser
# a chaque iteration de ma boucle

# https://www.w3schools.com/python/python_lists_comprehension.asp
