Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def convert(value, unit):
    conversions = {
        "cm": ("in", value / 2.54),
        "in": ("cm", value * 2.54),
        "yd": ("m", value * 0.9144),
        "m": ("yd", value / 0.9144),
        "oz": ("g", value * 28.3495),
        "g": ("oz", value / 28.3495),
        "lb": ("kg", value / 2.20462),
        "kg": ("lb", value * 2.20462)
    }
    if unit in conversions:
        new_unit, converted_value = conversions[unit]
        return f"{value} {unit} is equal to {converted_value:.2f} {new_unit}."
    else:
        return "Unknown unit. Please use valid units like cm, in, yd, m, oz, g, lb, kg."

    
user_input = input("Enter a distance or weight amount (e.g., '111.5 cm'): ").strip()
Enter a distance or weight amount (e.g., '111.5 cm'): 111.5 cm
>>> value_str, unit = user_input.split()
>>> value = float(value_str)
>>> result = convert(value, unit)
>>> print(result)
111.5 cm is equal to 43.90 in.
>>> user_input = input("Enter a distance or weight amount (e.g., '111.5 cm'): ").strip()
Enter a distance or weight amount (e.g., '111.5 cm'): 2.54 cm
>>> value_str, unit = user_input.split()
... value = float(value_str)
... result = convert(value, unit)
... print(result)
SyntaxError: multiple statements found while compiling a single statement
>>> value_str, unit = user_input.split()
>>> value = float(value_str)
>>> result = convert(value, unit)
>>> print(result)
2.54 cm is equal to 1.00 in.
>>> user_input = input("Enter a distance or weight amount (e.g., '111.5 cm'): ").strip()
Enter a distance or weight amount (e.g., '111.5 cm'): 1 yd
>>> value_str, unit = user_input.split()
>>> value = float(value_str)
>>> result = convert(value, unit)
>>> print(result)
1.0 yd is equal to 0.91 m.
>>> user_input = input("Enter a distance or weight amount (e.g., '111.5 cm'): ").strip()
Enter a distance or weight amount (e.g., '111.5 cm'): 1 oz
>>> value_str, unit = user_input.split()
>>> value = float(value_str)
>>> result = convert(value, unit)
>>> print(result)
1.0 oz is equal to 28.35 g.
>>> user_input = input("Enter a distance or weight amount (e.g., '111.5 cm'): ").strip()
Enter a distance or weight amount (e.g., '111.5 cm'): 1 lb
>>> value_str, unit = user_input.split()
>>> value = float(value_str)
>>> result = convert(value, unit)
>>> print(result)
1.0 lb is equal to 0.45 kg.
