import random
def password(special, uporlow, len):
    password = ""
    if special.lower() == "true":
        for x in range(len):
            password += chr(random.randint(33, 126))
    elif special.lower() == "false":
        for x in range(len):
            letter = str(random.randint(0,2))
            if letter == "0":
                letter = chr(random.randint(48, 57))
            elif letter == "1":
                letter = chr(random.randint(65, 90))
            elif letter == "2":
                letter = chr(random.randint(97, 122))
            password += letter
    if uporlow.lower() == "low":
        password = password.lower()
    elif uporlow.upper() == "up":
        password = password.upper()
    elif uporlow.lower() == "false":
        password = password
    return password