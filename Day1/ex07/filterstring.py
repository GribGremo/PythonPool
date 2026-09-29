import sys

def main() -> int :
    assert len(sys.argv) == 3, "Invalid number of arguments"
    assert type(sys.argv[1] is str), "First argument should be a string"
    assert type(sys.argv[2] is int), "Second argument should be an integer"


if __name__ == "__main__":
    main()

