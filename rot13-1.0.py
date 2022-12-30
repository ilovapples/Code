def encrypt(string):
    firstHalfLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    lastHalfLetters = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    encryptedString = ""
    selectedLetter = 0
    for x in range(len(string)):
        if string[selectedLetter] not in firstHalfLetters and string[selectedLetter] not in lastHalfLetters:
            encryptedString += string[selectedLetter]
            selectedLetter += 1
        else:
            if string[selectedLetter] in firstHalfLetters:
                encryptedString += lastHalfLetters[firstHalfLetters.index(string[selectedLetter])]
                selectedLetter += 1
            elif string[selectedLetter] in lastHalfLetters:
                encryptedString += firstHalfLetters[lastHalfLetters.index(string[selectedLetter])]
                selectedLetter += 1
    return encryptedString