def printTable():
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    row9 = []
    row10 = []
    number1 = 1
    number2 = 2
    number3 = 3
    number4 = 4
    number5 = 5
    number6 = 6
    number7 = 7
    number8 = 8
    number9 = 9
    number10 = 10
    for x in range(10):
        row1.append(number1)
        number1 += 1
    for x in range(10):
        row2.append(number2)
        number2 += 2
    for x in range(10):
        row3.append(number3)
        number3 += 3
    for x in range(10):
        row4.append(number4)
        number4 += 4
    for x in range(10):
        row5.append(number5)
        number5 += 5
    for x in range(10):
        row6.append(number6)
        number6 += 6
    for x in range(10):
        row7.append(number7)
        number7 += 7
    for x in range(10):
        row8.append(number8)
        number8 += 8
    for x in range(10):
        row9.append(number9)
        number9 += 9
    for x in range(10):
        row10.append(number10)
        number10 += 10
    
    print("_______________________________________________")
    print("|  |  01  02  03  04  05  06  07  08  09  10  |")
    print("|‾‾|‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|")
    print("|01|   %d   %d   %d   %d   %d   %d   %d   %d   %d  %d  |" % (row1[0], row1[1], row1[2], row1[3], row1[4], row1[5], row1[6], row1[7], row1[8], row1[9]))
    print("|02|   %d   %d   %d   %d  %d  %d  %d  %d  %d  %d  |" % (row2[0], row2[1], row2[2], row2[3], row2[4], row2[5], row2[6], row2[7], row2[8], row2[9]))
    print("|03|   %d   %d   %d  %d  %d  %d  %d  %d  %d  %d  |" % (row3[0], row3[1], row3[2], row3[3], row3[4], row3[5], row3[6], row3[7], row3[8], row3[9]))
    print("|04|   %d   %d  %d  %d  %d  %d  %d  %d  %d  %d  |" % (row4[0], row4[1], row4[2], row4[3], row4[4], row4[5], row4[6], row4[7], row4[8], row4[9]))
    print("|05|   %d  %d  %d  %d  %d  %d  %d  %d  %d  %d  |" % (row5[0], row5[1], row5[2], row5[3], row5[4], row5[5], row5[6], row5[7], row5[8], row5[9]))
    print("|06|   %d  %d  %d  %d  %d  %d  %d  %d  %d  %d  |" % (row6[0], row6[1], row6[2], row6[3], row6[4], row6[5], row6[6], row6[7], row6[8], row6[9]))
    print("|07|   %d  %d  %d  %d  %d  %d  %d  %d  %d  %d  |" % (row7[0], row7[1], row7[2], row7[3], row7[4], row7[5], row7[6], row7[7], row7[8], row7[9]))
    print("|08|   %d  %d  %d  %d  %d  %d  %d  %d  %d  %d  |" % (row8[0], row8[1], row8[2], row8[3], row8[4], row8[5], row8[6], row8[7], row8[8], row8[9]))
    print("|09|   %d  %d  %d  %d  %d  %d  %d  %d  %d  %d  |" % (row9[0], row9[1], row9[2], row9[3], row9[4], row9[5], row9[6], row9[7], row9[8], row9[9]))
    print("|10|  %d  %d  %d  %d  %d  %d  %d  %d  %d %d  |" % (row10[0], row10[1], row10[2], row10[3], row10[4], row10[5], row10[6], row10[7], row10[8], row10[9]))
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    
printTable()