from typing import List, Any, Dict

def zipmap(key_list: List[Any], value_list: List[Any], override: bool = False) -> Dict[Any, Any]:
    if not override and len(set(key_list)) != len(key_list):
        return {}

    zipped_pairs = zip(key_list, value_list + [None] * (len(key_list) - len(value_list)))
    result = {key: val for key, val in zipped_pairs}
    
    if override:
        return result
    else:
        if len(set(key_list)) != len(key_list):
            return {}
        return result

# Test cases
print(zipmap(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3, 4, 5, 6]))  
print(zipmap([1, 2, 3, 2], [4, 5, 6, 7], True))  
print(zipmap([1, 2, 3], [4, 5, 6, 7, 8]))  
print(zipmap([1, 3, 5, 7], [2, 4, 6])) 
