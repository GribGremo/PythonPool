import sys
import string

def main() ->int :
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----"
    }
    assert len(sys.argv) == 2, "Invalid number of arguments"
    assert all(c.isalpha() or c.isdigit() or c == " " for c in sys.argv[1]), "The arguments are bad"
    print(*map(lambda c: NESTED_MORSE[c.upper()], sys.argv[1]))

if __name__ == "__main__":
    main()

#NOTIONS
# all va iterer sur les elements de mon expression et me dire s'ils sont TOUS correct
#map permet de "creer " un resultat theorique d'une meme action effectuer sur tous les elements de iterable
# Dans mon cas je vais effectuer l'action "return NESTED_MORSE[c.upper()]" pour chaque iteration sur ma string sys.argv[1]
#Le * permet de decomposer mo objet iterable, il va print(elem1,elm2,elem3), c'est accesoirement ce qui met un espace entre chaque"caractere" morse