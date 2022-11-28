def rgb2hex(r, g, b):
    red1 = str(hex(r)).upper()
    if red1[-1] is red1[2]:
        red = '0' + red1[2]
    else:
        red = red1[2] + red1[3]
    green1 = str(hex(g)).upper()
    if green1[-1] is green1[2]:
        green = '0' + green1[2]
    else:
        green = green1[2] + green1[3]
    blue1 = str(hex(b)).upper()
    if blue1[-1] is blue1[2]:
        blue = '0' + blue1[2]
    else:
        blue = blue1[2] + blue1[3]
    return "#" + red + green + blue
converting = "y"
while converting == "y":
    print("\n\n" + rgb2hex(int(input("Red: ")), int(input("Green: ")), int(input("Blue: "))))
    converting = input("\nAgain?: ")
    if converting == "n":
        quit()