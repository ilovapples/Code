import random
from time import sleep

def correctlyCapitalize(s: str):
    """Returns a string with proper capitalization."""
    return s[0].upper() + s[1:].lower()

def randomlyCapitalize(s: str):
    """Returns a string with random capitalization."""
    final = ""
    for i in s:
        upOrLow = random.randint(0, 1)
        if upOrLow == 0:
            final += i.upper()
        else:
            final += i.lower()
    return final

randomlyCapitalized_Text = randomlyCapitalize("Hello, World")  
print(randomlyCapitalized_Text)
print(correctlyCapitalize(randomlyCapitalized_Text))
