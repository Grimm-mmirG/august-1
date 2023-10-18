def celsius_to_farenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

celsius = 25

# fahrenheit = celsius * 9/5 + 32
fahrenheit = celsius_to_farenheit(celsius)
print(f"{celsius} Celsius to Fahrenheit is {fahrenheit}")