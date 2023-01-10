def suminrange(lower: int, higher: int):
    total = 0
    for i in range(lower, higher+1):
        total += i
    return total

print(suminrange(int(input("Lower: ")), int(input("Higher: "))))