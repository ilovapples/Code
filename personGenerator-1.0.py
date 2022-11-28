# Python Code    Purpose: NULL
import random
for x in range(10000):
    randomFirst = random.randint(0, 6)
    randomLast = random.randint(0, 6)
    if randomFirst == 0:
        randomFirst = "Asher"
    elif randomFirst == 1:
        randomFirst = "Henry"
    elif randomFirst == 2:
        randomFirst = "Adam"
    elif randomFirst == 3:
        randomFirst = "Julia"
    elif randomFirst == 4:
        randomFirst = "Bob"
    elif randomFirst == 5:
        randomFirst = "Ted"
    else:
        randomFirst = "Joe"  
    if randomLast == 0:
        randomLast = "Grossman"
    elif randomLast == 1:
        randomLast = "Mason"
    elif randomLast == 2:
        randomLast = "Lewis"
    elif randomLast == 3:
        randomLast = "Glunt"
    elif randomLast == 4:
        randomLast = "Generic"
    elif randomLast == 5:
        randomLast = "Null"
    else:
        randomLast = "Mama"
    data = (randomFirst, randomLast, random.uniform(10, 1000), random.randint(0, 9))
    plural = ""
    if data[3] == 1:
        plural = ""
    else:
        plural = "s"
    print ("%s %s's balance is $%.2f, and they have %d sibling%s." % (data[0], data[1], data[2], data[3], plural))
    if randomLast == "Mama":
        if randomFirst == "Joe":
            print("HA" * 100)
