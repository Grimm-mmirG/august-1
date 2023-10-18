def celsius_to_farenheit(celsius):
    """ Given a celcius Value return a conversion"""
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
def f_to_c(f):
    """Given Farenheit value return conversion"""
    celsius = (f-32) * 5/9
    return celsius

celsius = 25
    
# fahrenheit = celsius * 9/5 + 32
fahrenheit = celsius_to_farenheit(celsius)
print(f"{celsius} Celsius to Fahrenheit is {fahrenheit}")

celsius = f_to_c(fahrenheit)
print(f"{fahrenheit} Fahrenheit to Celsius is {celsius}")