import random
def roll(count):
    rollFinal = 0
    for x in range(count):
        rollFinal += random.randint(1,6)
    return rollFinal
while True:
    print(roll(int(input("Roll Count: "))))