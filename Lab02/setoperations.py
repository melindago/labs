Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def make_set(data):
...     if data is None:
...         return[]
...     unique_list = []
...     for item in data:
...         if item not in unique_list:
...             unique_list.append(item)
...     return unique_list
... 
>>> print(make_set([1, 2, 3, 3, 4, 5, 5, 6, 7, 7]))
[1, 2, 3, 4, 5, 6, 7]
>>> def is_set(data):
...     if data is None:
...         return False
...     if len(data) == 0:
...         return True
...     return len(data) == len(make_set(data))
... 
>>> print(is_set([1, 2, 3, 4, 5]))
True
>>> def union(setA, setB):
...     if not is_set(setA) or not is_set(setB):
...         return []
...     combined_list = make_set(setA + setB)
...     return combined_list
... 
>>> print(union([1, 2], [2, 4], [2, 3]))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(union([1, 2], [2, 4], [2, 3]))
TypeError: union() takes 2 positional arguments but 3 were given
>>> print(union([2, 4], [1, 2]))
[2, 4, 1]
>>> def intersection(setA, setB):
...     if not is_set(setA) or not is_set(setB):
...         return []
...     intersect_list = []
... 
...     
>>> def intersection(setA, setB):
...     if not is_set(setA) or not is_set(setB):
...         return []
...     intersect_list = []
...     for item in setA:
...         if item in setB:
...             intersect_list.append(item)
...     return intersect_list
... 
>>> print(intersection([1, 2], [2, 3]))
[2]
