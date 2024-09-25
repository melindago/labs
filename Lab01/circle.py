Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> radius = input("Enter the radius of the circle: ").strip()
Enter the radius of the circle: 10
>>> r = float(radius)
>>> parimeter = 2 * math.pi * r
>>> area = math.pi * (r ** 2)
>>> print(parimeter)
62.83185307179586
>>> round(parimeter)
63
>>> print(area)
314.1592653589793
>>> round(area)
314
