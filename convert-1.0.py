convertFrom = input("Unit to convert from: ")
convertTo = input("Unit to convert to: ")
unitValue = float(input("Number of units: "))
convertedUnit = 0
if convertFrom == "celsius" or "Celsius" or "C" or "c":
    if convertTo == "fahrenheit" or "Fahrenheit" or "F" or "F":
        convertTo = "fahrenheit"
        convertedUnit = (unitValue / 5/9) + 32
    elif convertTo == "Kelvin" or "kelvin" or "k" or "K":
        convertTo = "kelvin"
        convertedUnit = unitValue + 273.15
elif convertFrom == "fahrenheit" or "Fahrenheit" or "F" or "F":
    if convertTo == "celsius" or "Celsius" or "C" or "c":
        convertTo = "celsius"
        convertedUnit = (unitValue - 32) * 5/9
    elif convertTo == "Kelvin" or "kelvin" or "k" or "K":
        convertTo = "Kelvin"
        convertedUnit = (unitValue - 32) * 5/9 + 273.15
elif convertFrom == "Kelvin" or "kelvin" or "k" or "K":
    if convertTo == "fahrenheit" or "Fahrenheit" or "F" or "f":
        convertTo = "fahrenheit"
        convertedUnit = (unitValue - 273.15) * 9/5 + 32
    elif convertTo == "celsius" or "Celsius" or "C" or "c":
        convertTo = "celsius"
        convertedUnit = unitValue - 273.15
print("%.5f %s in %s is %.5f %s." % (unitValue, convertFrom, convertTo, convertedUnit, convertTo))