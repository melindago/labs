Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> side_a = input("Enter the length of the first side: ").strip()
Enter the length of the first side: 5
>>> side_b = input("Enter the length of the second side: ").strip()
Enter the length of the second side: 12
>>> a = float(side_a)
>>> b = float(side_b)
>>> c = math.sqrt(a**2 + b**2)
>>> print(c)
13.0
