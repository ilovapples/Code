def upper(string):
    stringIndex = 0
    upperLetter = 0
    stringUpper = ""
    for x in range(len(string)):
        if string[stringIndex] == " ":
            stringUpper += " "
            stringIndex += 1
        elif ord(string[stringIndex]) < 123 and ord(string[stringIndex]) > 96:
            upperLetter = chr(ord(string[stringIndex]) - 32)
            stringUpper += upperLetter
            stringIndex += 1
        else:
            stringUpper += string[stringIndex]
            stringIndex += 1
    return stringUpper
def lower(string):
    stringIndex = 0
    lowerLetter = 0
    stringLower = ""
    for x in range(len(string)):
        if string[stringIndex] == " ":
            stringLower += " "
            stringIndex += 1
        elif ord(string[stringIndex]) < 91 and ord(string[stringIndex]) > 64:
            lowerLetter = chr(ord(string[stringIndex]) + 32)
            stringLower += lowerLetter
            stringIndex += 1
        else:
            stringLower += string[stringIndex]
            stringIndex += 1
    return stringLower