safetyStop = True
n = 25
x = n - 1
factorCount = 0     # Mutated: Y        Purpose: Choose how many factors to list, to eliminate factor over-padding.
factorSelect = 0    # Mutated: Y        Purpose: Choose save location for factors when found.
factors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]    # Mutated: Y        Purpose: Storing slots for saved factors.
# ⬇ Safety check to make sure n ≥ 3.
if n == 0:
    print("ERROR: n < 3")
elif n == 1:
    print("ERROR: n < 3")
elif n == 2:
    print("ERROR: n < 3")
else:
    if safetyStop == True:      # if safetyStop is on, it performs a quick check to see if the number is even.
        quickCheck = n / 2
        finalCheck = str(int(quickCheck)) + ".0"
        if finalCheck == str(quickCheck):
            print("%d is definitely composite because %.5f ÷ 2 = %f" % (n, n, quickCheck))
        else:
            isPrimeConfirmation = 0
            primeCheck = 0.0
            primeCheckcutOff = ""
            while x != 1:       # Repeats a function to check if x is currently a factor of n.
                primeCheck = n / x
                primeCheckcutOff = str(int(primeCheck)) + ".0"
                if primeCheckcutOff == str(primeCheck):
                    print("%d is composite: %d ÷ %d = %d" % (n, n, x, primeCheck))
                    isPrimeConfirmation += 1
                    if factorSelect == 0:           # Chooses which slot to store factors in.
                        factors[0] = primeCheck
                    elif factorSelect == 1:
                        factors[1] = primeCheck
                    elif factorSelect == 2:
                        factors[2] = primeCheck
                    elif factorSelect == 3:
                        factors[3] = primeCheck
                    elif factorSelect == 4:
                        factors[4] = primeCheck
                    elif factorSelect == 5:
                        factors[5] = primeCheck
                    elif factorSelect == 6:
                        factors[6] = primeCheck
                    elif factorSelect == 7:
                        factors[7] = primeCheck
                    elif factorSelect == 8:
                        factors[8] = primeCheck
                    elif factorSelect == 9:
                        factors[9] = primeCheck
                    elif factorSelect == 10:
                        factors[10] = primeCheck
                    elif factorSelect == 11:
                        factors[11] = primeCheck
                    elif factorSelect == 12:
                        factors[12] = primeCheck
                    elif factorSelect == 13:
                        factors[13] = primeCheck
                    elif factorSelect == 14:
                        factors[14] = primeCheck
                    elif factorSelect == 15:
                        factors[15] = primeCheck
                    elif factorSelect == 16:
                        factors[16] = primeCheck
                    elif factorSelect == 17:
                        factors[17] = primeCheck
                    elif factorSelect == 18:
                        factors[18] = primeCheck
                    elif factorSelect == 19:
                        factors[19] = primeCheck
                    elif factorSelect == 20:
                        factors[20] = primeCheck
                    elif factorSelect == 21:
                        factors[21] = primeCheck
                    elif factorSelect == 22:
                        factors[22] = primeCheck
                    elif factorSelect == 23:
                        factors[23] = primeCheck
                    elif factorSelect == 24:
                        factors[24] = primeCheck
                    elif factorSelect == 25:
                        factors[25] = primeCheck
                    elif factorSelect == 26:
                        factors[26] = primeCheck
                    elif factorSelect == 27:
                        factors[27] = primeCheck
                    elif factorSelect == 28:
                        factors[28] = primeCheck
                    elif factorSelect == 29:
                        factors[29] = primeCheck
                    elif factorSelect == 30:
                        factors[30] = primeCheck
                    elif factorSelect == 31:
                        factors[31] = primeCheck
                    elif factorSelect == 32:
                        factors[32] = primeCheck
                    elif factorSelect == 33:
                        factors[33] = primeCheck
                    elif factorSelect == 34:
                        factors[34] = primeCheck
                    elif factorSelect == 35:
                        factors[35] = primeCheck
                    elif factorSelect == 36:
                        factors[36] = primeCheck
                    elif factorSelect == 37:
                        factors[37] = primeCheck
                    elif factorSelect == 38:
                        factors[38] = primeCheck
                    elif factorSelect == 39:
                        factors[39] = primeCheck
                    factorSelect += 1
                else:
                    print("%d is not YET composite." % n)
                x -= 1
            if isPrimeConfirmation == 0:
                print("%d is definitely prime!" % n)
            elif isPrimeConfirmation > 0:
                print("%d is definitely composite." % n)
    elif safetyStop == False:
            isPrimeConfirmation = 0
            primeCheck = 0.0
            primeCheckcutOff = ""
            while x != 1:
                primeCheck = n / x
                primeCheckcutOff = str(int(primeCheck)) + ".0"
                if primeCheckcutOff == str(primeCheck):
                    print("%d is composite: %d ÷ %d = %d" % (n, n, x, primeCheck))
                    isPrimeConfirmation += 1
                    if factorSelect == 0:
                        factors[0] = primeCheck
                    elif factorSelect == 1:
                        factors[1] = primeCheck
                    elif factorSelect == 2:
                        factors[2] = primeCheck
                    elif factorSelect == 3:
                        factors[3] = primeCheck
                    elif factorSelect == 4:
                        factors[4] = primeCheck
                    elif factorSelect == 5:
                        factors[5] = primeCheck
                    elif factorSelect == 6:
                        factors[6] = primeCheck
                    elif factorSelect == 7:
                        factors[7] = primeCheck
                    elif factorSelect == 8:
                        factors[8] = primeCheck
                    elif factorSelect == 9:
                        factors[9] = primeCheck
                    elif factorSelect == 10:
                        factors[10] = primeCheck
                    elif factorSelect == 11:
                        factors[11] = primeCheck
                    elif factorSelect == 12:
                        factors[12] = primeCheck
                    elif factorSelect == 13:
                        factors[13] = primeCheck
                    elif factorSelect == 14:
                        factors[14] = primeCheck
                    elif factorSelect == 15:
                        factors[15] = primeCheck
                    elif factorSelect == 16:
                        factors[16] = primeCheck
                    elif factorSelect == 17:
                        factors[17] = primeCheck
                    elif factorSelect == 18:
                        factors[18] = primeCheck
                    elif factorSelect == 19:
                        factors[19] = primeCheck
                    elif factorSelect == 20:
                        factors[20] = primeCheck
                    elif factorSelect == 21:
                        factors[21] = primeCheck
                    elif factorSelect == 22:
                        factors[22] = primeCheck
                    elif factorSelect == 23:
                        factors[23] = primeCheck
                    elif factorSelect == 24:
                        factors[24] = primeCheck
                    elif factorSelect == 25:
                        factors[25] = primeCheck
                    elif factorSelect == 26:
                        factors[26] = primeCheck
                    elif factorSelect == 27:
                        factors[27] = primeCheck
                    elif factorSelect == 28:
                        factors[28] = primeCheck
                    elif factorSelect == 29:
                        factors[29] = primeCheck
                    elif factorSelect == 30:
                        factors[30] = primeCheck
                    elif factorSelect == 31:
                        factors[31] = primeCheck
                    elif factorSelect == 32:
                        factors[32] = primeCheck
                    elif factorSelect == 33:
                        factors[33] = primeCheck
                    elif factorSelect == 34:
                        factors[34] = primeCheck
                    elif factorSelect == 35:
                        factors[35] = primeCheck
                    elif factorSelect == 36:
                        factors[36] = primeCheck
                    elif factorSelect == 37:
                        factors[37] = primeCheck
                    elif factorSelect == 38:
                        factors[38] = primeCheck
                    elif factorSelect == 39:
                        factors[39] = primeCheck
                    factorSelect += 1
                else:
                    print("%d is not YET composite." % n)
                x -= 1
            if isPrimeConfirmation == 0:
                print("%d is definitely prime!" % n)
            elif isPrimeConfirmation > 0:
                print("%d is definitely composite." % n)
    else:
        print("Invalid value for safetyStop. Please input True or False.")
    if factors[0] != 0:
        factorCount += 1
    if factors[1] != 0:
        factorCount += 1
    if factors[2] != 0:
        factorCount += 1
    if factors[3] != 0:
        factorCount += 1
    if factors[4] != 0:
        factorCount += 1
    if factors[5] != 0:
        factorCount += 1
    if factors[6] != 0:
        factorCount += 1
    if factors[7] != 0:
        factorCount += 1
    if factors[8] != 0:
        factorCount += 1
    if factors[9] != 0:
        factorCount += 1
    if factors[10] != 0:
        factorCount += 1
    if factors[11] != 0:
        factorCount += 1
    if factors[12] != 0:
        factorCount += 1
    if factors[13] != 0:
        factorCount += 1
    if factors[14] != 0:
        factorCount += 1
    if factors[15] != 0:
        factorCount += 1
    if factors[16] != 0:
        factorCount += 1
    if factors[17] != 0:
        factorCount += 1
    if factors[18] != 0:
        factorCount += 1
    if factors[19] != 0:
        factorCount += 1
    if factors[20] != 0:
        factorCount += 1
    if factors[21] != 0:
        factorCount += 1
    if factors[22] != 0:
        factorCount += 1
    if factors[23] != 0:
        factorCount += 1
    if factors[24] != 0:
        factorCount += 1
    if factors[25] != 0:
        factorCount += 1
    if factors[26] != 0:
        factorCount += 1
    if factors[27] != 0:
        factorCount += 1
    if factors[28] != 0:
        factorCount += 1
    if factors[29] != 0:
        factorCount += 1
    if factors[30] != 0:
        factorCount += 1
    if factors[31] != 0:
        factorCount += 1
    if factors[32] != 0:
        factorCount += 1
    if factors[33] != 0:
        factorCount += 1
    if factors[34] != 0:
        factorCount += 1
    if factors[35] != 0:
        factorCount += 1
    if factors[36] != 0:
        factorCount += 1
    if factors[37] != 0:
        factorCount += 1
    if factors[38] != 0:
        factorCount += 1
    if factors[39] != 0:
        factorCount += 1
    
    if factorCount == 0:
        print("%d has no factors because it is prime!" % n)
    if factorCount == 1:
        print("%d's %d factor is %d." % (n, factorCount, factors[0]))
    if factorCount == 2:
        print("%d's %d factors are %d and %d."  % (n, factorCount, factors[0], factors[1]))
    if factorCount == 3:
        print("%d's %d factors are %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2]))
    if factorCount == 4:
        print("%d's %d factors are %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3]))
    if factorCount == 5:
        print("%d's %d factors are %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4]))
    if factorCount == 6:
        print("%d's %d factors are %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5]))
    if factorCount == 7:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6]))
    if factorCount == 8:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7]))
    if factorCount == 9:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8]))
    if factorCount == 10:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9]))
    if factorCount == 11:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10]))
    if factorCount == 12:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11]))
    if factorCount == 13:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12]))
    if factorCount == 14:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13]))
    if factorCount == 15:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14]))
    if factorCount == 16:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15]))
    if factorCount == 17:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16]))
    if factorCount == 18:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17]))
    if factorCount == 19:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18]))
    if factorCount == 20:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19]))
    if factorCount == 21:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20]))
    if factorCount == 22:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21]))
    if factorCount == 23:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22]))
    if factorCount == 24:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23]))
    if factorCount == 25:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24]))
    if factorCount == 26:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25]))
    if factorCount == 27:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25], factors[26]))
    if factorCount == 28:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25], factors[26], factors[27]))
    if factorCount == 29:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25], factors[26], factors[27], factors[28]))
    if factorCount == 30:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25], factors[26], factors[27], factors[28], factors[29]))
    if factorCount == 31:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25], factors[26], factors[27], factors[28], factors[29], factors[30]))
    if factorCount == 32:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25], factors[26], factors[27], factors[28], factors[29], factors[30], factors[31]))
    if factorCount == 33:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25], factors[26], factors[27], factors[28], factors[29], factors[30], factors[31], factors[32]))
    if factorCount == 34:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25], factors[26], factors[27], factors[28], factors[29], factors[30], factors[31], factors[32], factors[33]))
    if factorCount == 35:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25], factors[26], factors[27], factors[28], factors[29], factors[30], factors[31], factors[32], factors[33], factors[34]))
    if factorCount == 36:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25], factors[26], factors[27], factors[28], factors[29], factors[30], factors[31], factors[32], factors[33], factors[34], factors[35]))
    if factorCount == 37:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25], factors[26], factors[27], factors[28], factors[29], factors[30], factors[31], factors[32], factors[33], factors[34], factors[35], factors[36]))
    if factorCount == 38:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25], factors[26], factors[27], factors[28], factors[29], factors[30], factors[31], factors[32], factors[33], factors[34], factors[35], factors[36], factors[37]))
    if factorCount == 39:
        print("%d's %d factors are %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, and %d."  % (n, factorCount, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8], factors[9], factors[10], factors[11], factors[12], factors[13], factors[14], factors[15], factors[16], factors[17], factors[18], factors[19], factors[20], factors[21], factors[22], factors[23], factors[24], factors[25], factors[26], factors[27], factors[28], factors[29], factors[30], factors[31], factors[32], factors[33], factors[34], factors[35], factors[36], factors[37], factors[38]))
