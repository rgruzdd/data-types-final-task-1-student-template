from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    """
    Add your code here or call it from here   
    """
    new_list = []
    for i in lst:
        for value in i.values():
            if value not in new_list:
                new_list.append(value)


    return new_list

    pass

