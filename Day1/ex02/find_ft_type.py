from typing import Any  

def all_thing_is_obj(object:Any) -> int:
    t = type(object)
    if t == str:
        print(f"{object} is in the kitchen : {t}")
    elif t == list:
        print(f"List : {t}")
    elif t == tuple:
        print(f"Tuple : {t}")
    elif t == set:
        print(f"Set : {t}")
    elif t == dict:
        print(f"Dict : {t}")
    else:
        print("Type not found")
        
    return 42

#https://www.geeksforgeeks.org/python/python-type-function/