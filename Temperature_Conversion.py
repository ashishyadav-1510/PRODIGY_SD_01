
def celsius_to_fahrenheit(c):
    return ((c * 9/5) + 32)

def celsius_to_kelvin(c):
    return (c + 273.15)

def fahrenheit_to_celsius(f):
    return ((f - 32) * 5/9)

def fahrenheit_to_kelvin(f):
    return (((f - 32) * 5/9)+ 273.15)

def kelvin_to_celsius(k):
    return (k - 273.15)

def kelvin_to_fahrenheit(k):
    return (((k - 273.15) * 9/5) + 32)

def convert_temperature(value, unit):
    unit = unit.lower()
    
    if(unit == "celsius" or unit == "c"):
        print(f"Entered Temperature: {value}°C")
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        print(f"Converted Temperature in other units: {round(f,2)}°F = {round(k,2)}K")

    elif(unit == "fahrenheit" or unit == "f"):
        print(f"Entered Temperature: {value}°F")
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        print(f"Converted Temperature in other units: {round(c,2)}°C = {round(k,2)}K")

    elif(unit == "kelvin" or unit == "k"):
        print(f"Entered Temperature: {value}K")
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        print(f"Converted Temperature in other units: {round(c,2)}°C = {round(f,2)}°F")
    
    else:
        print("Invalid unit! Should not happen if input is validated.")

print("*** Temperature Conversion Program ***")

while True:
    try:
        temp = float(input("Enter Value of Temperature = "))
        break
    except ValueError:
        print("!!Invalid Temperature!!\nPlease enter a valid Temperature(hint: numeric or float)")

while True:
    unit = input("Enter Unit of Temperature (celsius,fahrenheit,kelvin)= ").lower()
    if(unit in ["celsius","c","fahrenheit","f","kelvin","k"]):
        break
    else:
        print("!!Wrong Unit!!\nPlease enter a valid Unit of Temperature (hint: Celcius, Fahrenheit, Kelvin)")

convert_temperature(temp, unit)