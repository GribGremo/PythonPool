"""This is module documentation"""

def main() -> int:
    """This my my main function"""
    print(__doc__)
    print(main.__doc__)
    return 1

if __name__ == "__main__":
    main()