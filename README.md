# Temperature Conversion Program

A simple and interactive Python program to convert temperatures between **Celsius**, **Fahrenheit**, and **Kelvin**. This beginner-friendly project demonstrates conditional logic, functions, and user input validation in Python.

## Features

- Converts temperature values between **Celsius**, **Fahrenheit**, and **Kelvin**
- Accepts user input with input validation for both temperature and unit
- Supports case-insensitive unit input like `celsius`, `C`, `fahrenheit`, `F`, etc.
- Displays neatly formatted output with rounded values
- Beginner-friendly code and modular structure using functions

## How It Works

### 1. Input from User

The program asks the user to input:

- A temperature value (must be a valid number)
- The unit of the temperature (`celsius`, `fahrenheit`, `kelvin` or their short forms: `c`, `f`, `k`)

Invalid inputs trigger re-prompts until the correct format is entered.

### 2. Conversion Logic

Based on the entered unit, the program uses corresponding formulas:

| From → To            | Formula                       |
| --------------------- | ----------------------------- |
| Celsius → Fahrenheit | (°C × 9/5) + 32             |
| Celsius → Kelvin     | °C + 273.15                  |
| Fahrenheit → Celsius | (°F − 32) × 5/9            |
| Fahrenheit → Kelvin  | ((°F − 32) × 5/9) + 273.15 |
| Kelvin → Celsius     | K − 273.15                   |
| Kelvin → Fahrenheit  | ((K − 273.15) × 9/5) + 32   |

## Code Overview

### Conversion Functions

```python
def celsius_to_fahrenheit(c): return ((c * 9/5) + 32)
def celsius_to_kelvin(c): return (c + 273.15)
def fahrenheit_to_celsius(f): return ((f - 32) * 5/9)
def fahrenheit_to_kelvin(f): return (((f - 32) * 5/9) + 273.15)
def kelvin_to_celsius(k): return (k - 273.15)
def kelvin_to_fahrenheit(k): return (((k - 273.15) * 9/5) + 32)
```

## ScreenShots

### Explaination

1. **Temperature Conversion Functions**
   These are basic mathematical functions that convert temperature from one unit to another.

def celsius_to_fahrenheit(c):
    return ((c * 9/5) + 32)
Converts Celsius to Fahrenheit

Formula: (°C × 9/5) + 32 = °F

def celsius_to_kelvin(c):
    return (c + 273.15)
Converts Celsius to Kelvin

Formula: °C + 273.15 = K

def fahrenheit_to_celsius(f):
    return ((f - 32) * 5/9)
Converts Fahrenheit to Celsius

Formula: (°F − 32) × 5/9 = °C

def fahrenheit_to_kelvin(f):
    return (((f - 32) * 5/9)+ 273.15)
Converts Fahrenheit to Kelvin

Formula: (°F − 32) × 5/9 + 273.15 = K

def kelvin_to_celsius(k):
    return (k - 273.15)
Converts Kelvin to Celsius

Formula: K − 273.15 = °C

def kelvin_to_fahrenheit(k):
    return (((k - 273.15) * 9/5) + 32)
Converts Kelvin to Fahrenheit

Formula: (K − 273.15) × 9/5 + 32 = °F

2. **Main Conversion Logic**

def convert_temperature(value, unit):
    unit = unit.lower()
This function takes a numeric value and its unit (C, F, or K).

It converts the unit to lowercase for consistency ("C" becomes "c").

If input is Celsius:

    if(unit == "celsius" or unit == "c"):
        print(f"Entered Temperature: {value}°C")
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        print(f"Converted Temperature in other units: {round(f,2)}°F = {round(k,2)}K")
Calls the conversion functions to convert Celsius to Fahrenheit and Kelvin.

Displays the result using round() to format to 2 decimal places.

If input is Fahrenheit:

    elif(unit == "fahrenheit" or unit == "f"):
        print(f"Entered Temperature: {value}°F")
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        print(f"Converted Temperature in other units: {round(c,2)}°C = {round(k,2)}K")
Converts Fahrenheit to Celsius and Kelvin.

If input is Kelvin:

    elif(unit == "kelvin" or unit == "k"):
        print(f"Entered Temperature: {value}K")
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        print(f"Converted Temperature in other units: {round(c,2)}°C = {round(f,2)}°F")
Converts Kelvin to Celsius and Fahrenheit.

Invalid Unit:

    else:
        print("Invalid unit! Should not happen if input is validated.")
Fallback in case an invalid unit somehow reaches here.

3. **Program Starts Here**

print("*** Temperature Conversion Program ***")
Display welcome message

4. **User Input: Temperature Value**

while True:
    try:
        temp = float(input("Enter Value of Temperature = "))
        break
    except ValueError:
        print("!!Invalid Temperature!!\nPlease enter a valid Temperature(hint: numeric or float)")
Repeatedly prompts the user for a numeric temperature value.

Uses try-except to handle invalid inputs (non-numeric strings).

5. **User Input: Temperature Unit**

while True:
    unit = input("Enter Unit of Temperature (celsius,fahrenheit,kelvin)= ").lower()
    if(unit in ["celsius","c","fahrenheit","f","kelvin","k"]):
        break
    else:
        print("!!Wrong Unit!!\nPlease enter a valid Unit of Temperature (hint: Celcius, Fahrenheit, Kelvin)")
Asks for the unit of the input temperature.

Accepts multiple variations like "c" or "celsius", etc.

Keeps prompting until a valid unit is entered.

6. **Final Call to Conversion Function**

convert_temperature(temp, unit)
Once the temperature and its unit are successfully captured, it calls the main logic to do the conversion and print results.

Sample Output

*** Temperature Conversion Program ***
Enter Value of Temperature = 100
Enter Unit of Temperature (celsius,fahrenheit,kelvin)= celsius
Entered Temperature: 100.0°C
Converted Temperature in other units: 212.0°F = 373.15K
