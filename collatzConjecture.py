def run(seed):
    iteration = 0
    final = ""
    num = seed
    padding = 0
    while num != 1:
        final = f"{iteration}: {str(int(num))}"
        padding = 25 - len(final)
        final = f"{iteration}:" + " " * padding + f"{str(int(num))}"
        if num%2 == 0:
            num /= 2
            iteration += 1
            print(final)
        else:
            num = num * 3 + 1
            iteration += 1
            print(final)
            


    final = f"{iteration}: {str(int(num))}"
    padding = 25 - len(final)
    final = f"{iteration}:" + " " * padding + f"{str(int(num))}"    
    print(final)
run(75381347813471635471863547816351876317835614738546187356147385146378561357861837456139516439541635197643517193617316931643196146375139005719813472951983257902836982371698123751723967219386713298671293867298316798327598237692386159812365927138757812369821377326)