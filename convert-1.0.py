convertFrom = input("Unit to convert from: ")
convertTo = input("Unit to convert to: ")
unitValue = float(input("Number of units: "))
convertedUnit = 0
def cToF(unitValue):
    return (unitValue / 5/9) + 32
def cToK(unitValue):
    return unitValue + 273.15
def fToC(unitValue):
    return (unitValue - 32) * 5/9
def fToK(unitValue):
    return (unitValue - 32) * 5/9 + 273.15
def kToF(unitValue):
    return (unitValue - 273.15) * 9/5 + 32
def kToC(unitValue):
    return unitValue - 273.15
def binToDec(input):
    index = -1
    decimal = 0
    decimalAdding = 1
    for x in range(len(input)):
        if input[index] == "1":
            decimal += decimalAdding
        decimalAdding *= 2
        index -= 1
    return decimal

if convertFrom == "celsius" or "Celsius" or "C" or "c":
    if convertTo == "fahrenheit" or "Fahrenheit" or "F" or "F":
        convertTo = "fahrenheit"
        convertedUnit = cToF(unitValue)
    elif convertTo == "Kelvin" or "kelvin" or "k" or "K":
        convertTo = "kelvin"
        convertedUnit = cToK(unitValue)
        
        
elif convertFrom == "fahrenheit" or "Fahrenheit" or "F" or "F":
    if convertTo == "celsius" or "Celsius" or "C" or "c":
        convertTo = "celsius"
        convertedUnit = fToC(unitValue)
    elif convertTo == "Kelvin" or "kelvin" or "k" or "K":
        convertTo = "Kelvin"
        convertedUnit = fToK(unitValue)
        
        
elif convertFrom == "Kelvin" or "kelvin" or "k" or "K":
    if convertTo == "fahrenheit" or "Fahrenheit" or "F" or "f":
        convertTo = "fahrenheit"
        convertedUnit = kToF(unitValue)
    elif convertTo == "celsius" or "Celsius" or "C" or "c":
        convertTo = "celsius"
        convertedUnit = kToC(unitValue)


elif convertFrom == "binary" or "Binary" or "b" or "B":
    print("%s = %s." % (unitValue, binToDec(unitValue)))
    
print("%.5f %s in %s is %.5f %s." % (unitValue, convertFrom, convertTo, convertedUnit, convertTo))