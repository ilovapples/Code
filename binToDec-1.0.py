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
print(binToDec(input("Binary: ")))