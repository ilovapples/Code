num1:float = 2.0
num2:float = 15.0
num3:float = 1.0
operation1 = "^"
operation2 = "-"
output = 0.0

if num3 == 0.0:       # Checks to see if a third variable is in play.
    if operation1 == "+":
        output = num1 + num2
        print("%.4f %s %.4f = %.4f" % (num1, operation1, num2, output))
    elif operation1 == "-":
        output = num1 - num2
        print("%.4f %s %.4f = %.4f" % (num1, operation1, num2, output))
    elif operation1 == "*":
        output = num1 * num2
        print("%.4f %s %.4f = %.4f" % (num1, operation1, num2, output))
    elif operation1 == "/":
        output = num1 / num2
        print("%.4f %s %.4f = %.4f" % (num1, operation1, num2, output))
    elif operation1 == "^":
        output = num1 ** num2
        print("%.4f %s %.4f = %.4f" % (num1, operation1, num2, output))
    elif operation1 == "root":
        output == num1 ** (1.0 / num2)
        print("%.4f√%.4f = %.4f" % (num1, num2, output))
elif num3 != 0:
    if operation1 == "+":
        if operation2 == "+":
            output = num1 + num2 + num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "-":
            output = num1 + num2 - num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "*":
            output = num1 + num2 * num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "/":
            output = num1 + num2 / num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "^":
            output = num1 + num2 ^ num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "root":
            output = num1 + (num2**(1.0/num3))
            print("%.4f %s %.4f√%.4f = %.4f" % (num1, operation1, num2, num3, output))
    elif operation1 == "-":
        if operation2 == "+":
            output = num1 - num2 + num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "-":
            output = num1 - num2 - num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "*":
            output = num1 - num2 * num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "/":
            output = num1 - num2 / num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "^":
            output = num1 - num2 ^ num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "root":
            output = num1 - (num2**(1.0/num3))
            print("%.4f %s %.4f√%.4f = %.4f" % (num1, operation1, num2, num3, output))
    elif operation1 == "*":
        if operation2 == "+":
            output = num1 * num2 + num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "-":
            output = num1 * num2 - num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "*":
            output = num1 * num2 * num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "/":
            output = num1 * num2 / num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "^":
            output = num1 * num2 ^ num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "root":
            output = num1 * (num2**(1.0/num3))
            print("%.4f %s %.4f√%.4f = %.4f" % (num1, operation1, num2, num3, output))
    elif operation1 == "/":
        if operation2 == "+":
            output = num1 / num2 + num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "-":
            output = num1 / num2 - num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "*":
            output = num1 / num2 * num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "/":
            output = num1 / num2 / num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "^":
            output = num1 / num2 ^ num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "root":
            output = num1 / (num2**(1.0/num3))
            print("%.4f %s %.4f√%.4f = %.4f" % (num1, operation1, num2, num3, output))
    elif operation1 == "^":
        if operation2 == "+":
            output = num1 ** num2 + num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "-":
            output = num1 ** num2 - num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "*":
            output = num1 ** num2 * num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "/":
            output = num1 ** num2 / num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "^":
            output = num1 ** num2 ^ num3
            print("%.4f %s %.4f %s %.4f = %.4f" % (num1, operation1, num2, operation2, num3, output))
        elif operation2 == "root":
            output = num1 ** (num2**(1.0/num3))
            print("%.4f %s %.4f√%.4f = %.4f" % (num1, operation1, num2, num3, output))
    elif operation1 == "root":
        if operation2 == "+":
            output = (num1**(1.0/num2)) + num3
            print("%.4f√%.4f %s %.4f = %.4f" % (num1, num2, operation2, num3, output))
        elif operation2 == "-":
            output = (num1**(1.0/num2)) - num3
            print("%.4f√%.4f %s %.4f = %.4f" % (num1, num2, operation2, num3, output))
        elif operation2 == "*":
            output = (num1**(1.0/num2)) * num3
            print("%.4f√%.4f %s %.4f = %.4f" % (num1, num2, operation2, num3, output))
        elif operation2 == "/":
            output = (num1**(1.0/num2)) / num3
            print("%.4f√%.4f %s %.4f = %.4f" % (num1, num2, operation2, num3, output))
        elif operation2 == "^":
            output = (num1**(1.0/num2)) ^ num3
            print("%.4f√%.4f %s %.4f = %.4f" % (num1, num2, operation2, num3, output))
        elif operation2 == "root":
            output = (num1**(1.0/(num2**(1.0/num3))))
            print("%.4f√(%.4f√%.4f) = %.4f" % (num1, num2, num3, output))
