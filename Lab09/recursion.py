
def product_of_digits(x):
    x = abs(x) 
    if x < 10:
        return x
    else:
        return (x % 10) * product_of_digits(x // 10)

print(product_of_digits(234))  
print(product_of_digits(-12))
print(product_of_digits(12))
print(product_of_digits(987654321))
print(product_of_digits(10000))

def array_to_string(a, index=0):
    if not a:
        return ""
    if index == len(a) - 1:
        return str(a[index])
    return str(a[index]) + "," + array_to_string(a, index + 1)

print(array_to_string([1, 2, 3, 4]))
print(array_to_string([10, 20, 30]))
print(array_to_string([100, 200, 300, 400]))
print(array_to_string([7]))            
print(array_to_string([]))

def log(base, value, count=0):
    if value <= 0 or base <= 1:
        raise ValueError("Value must be greater than 0 and base must be greater than 1")
    if value < base:
        return count
    return log(base, value // base, count + 1)

print(log(10, 123456)) 
print(log(2, 64))
print(log(10, 4567))
print(log(10, 100000000))

