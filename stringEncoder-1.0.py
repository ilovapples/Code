import random
inputStringContinues = "y"
while inputStringContinues == "y":
    string = input("Text: ")
    stringLength = len(string)
    encodedString = ""
    lastChar = string[stringLength - 1]
    for x in range(stringLength):
        encodedString += chr(random.randint(33, 250))
    print("%s to %s" % (string, encodedString))
    inputStringContinues = input("Input another string? (y/n)")