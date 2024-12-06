from functools import reduce
from typing import Callable, List, Any

def filter_with_reduce(predicate: Callable[[Any], bool], target_list: List[Any]) -> List[Any]:
    return reduce(lambda acc, x: acc + [x] if predicate(x) else acc, target_list, [])

# Test case
print(filter_with_reduce(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])) 
print(filter_with_reduce(lambda x: x > 3, [1, 2, 3, 4, 5])) 
