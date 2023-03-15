from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    """
    Add your code here or call it from here   
    """
    new_set = set()
    for i in lst:
        for value in i.values():
            new_set.add(value)
    return new_set


