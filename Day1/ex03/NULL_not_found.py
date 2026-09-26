from typing import Any

def NULL_not_found(object: Any) -> int:
    t = type(object)

    if object is None:
        print(f"Nothing: None {t}")
    elif isinstance(object, float) and object != object:#
        print(f"Cheese: nan {t}")
    elif isinstance(object,int) and object == 0:
        print(f"Zero: 0 {t}")
    elif object == "" :#
        print(f"Empty: {t}")
    elif isinstance(object,bool) and object is False:
        print(f"False: False {t}")
    else:
        print("Type not found")
        return 1


# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$

#NOTION
#isinstance Pour savoir si un objet correspond a un type on peut faire object == type(toto) mais isinstance permet de verifier y compris les types heritees donc on preferera a l'avenir 
#Attention bool est une sous classe de int il faut bien s'assurer de ces 2 types
#Un NaN est considere comme different de lui meme etant donne que ces chiffres ne sont pas representables