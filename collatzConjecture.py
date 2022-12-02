index = 0
indexF = str(index)
while True:
    n = int(input("Input: "))
    print("000: %s" % n)
    for x in range(int(n)):
        if (n%2) == 0:
            index += 1
            if index < 100:
                if index < 10:
                    indexF = "00" + str(index)
                elif index > 9:
                    indexF = "0" + str(index)
            elif index > 99:
                indexF = str(index)
            n /= 2
            print("%s: %d" % (indexF, n))
            if n == 1:
                print("END")
                break
        elif (n%2) != 0:
            index += 1
            if index < 100:
                if index < 10:
                    indexF = "00" + str(index)
                elif index > 9:
                    indexF = "0" + str(index)
            elif index > 99:
                indexF = str(index)
            n = (3*n) + 1
            print("%s: %d" % (indexF, n))
    index = 0