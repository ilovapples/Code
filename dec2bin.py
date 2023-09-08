from math import *

def d2b(n: int):
    bits = 1
    while bits < n:
        bits *= 2
    bits = int(bits/2)
    
    temps = []
    for i in range(int(log(bits, 2))):
        temps.append(int(bits/(2**i)))
    if not 1 in temps:
        temps.append(1)
    ip = [[0, i] for i in temps]
    finals = [[0, 0] for i in range(len(temps))]
    
    for index, i in enumerate(ip):
        if 
        finals[index] = 
    
    return [bits,ip,temps]

while True:
    try:
        print(d2b(int(input("Num: "))))
        break
    except ValueError:
        continue