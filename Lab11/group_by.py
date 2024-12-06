from typing import Callable, List, Any, Dict

def group_by(f: Callable[[Any], Any], target_list: List[Any]) -> Dict[Any, List[Any]]:
    grouped_dict = {}
    for item in target_list:
        key = f(item)
        if key not in grouped_dict:
            grouped_dict[key] = []
        grouped_dict[key].append(item)
    return grouped_dict

# Test case
print(group_by(len, ["hi", "dog", "me", "bad", "good"]))
