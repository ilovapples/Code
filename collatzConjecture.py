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
run(15)