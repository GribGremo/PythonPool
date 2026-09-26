import sys


def whatis(arg) -> None:
    if arg % 2 == 0:
        print("I'm even")
    else:
        print("I'm odd")
        
if __name__ == "__main__":
    nb = None

    assert len(sys.argv) > 1, "one integer is needed as argument"
    assert len(sys.argv) < 3, "more than one argument is provided"
    try:
        nb = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    # assert type(sys.argv[1]) is int, "argument is not an integer"
    # cp_arg = sys.argv[1:]
    whatis(nb)


#NOTIONS
#En python pas de fonction main obligatoire mais la convention veut que l'on 
# verifie le nom du fichier dans la variable "__name__", si ce fichier a ete
# execute directement le name sera alors "__main__", vous pourrez alors 
# verifier le nom de main avant d'executer ce fichier,
# il pourrait tout simplement etre importe depuis un autre fichier
# et appeler ce qui pourrait causer des soucis.
# Attention en python on envoie des references dans les fonctions pas des copies

#Assert verify an assumption is x > 2 everything fine, no then it's over

#try except: similaire a try catch sauf que ca ne me fai tpas sortir du programme