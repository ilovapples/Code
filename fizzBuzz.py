def fizzBuzz(upton: int):
    for i in range(0, upton+1):
        if i == 0 or i == 1 or i == 3 or i == 5:
            print(i)
        else:
            if i%3 == 0 and i%5 == 0:
                print("FizzBuzz")
            elif i%3 == 0:
                print("Fizz")
            elif i%5 == 0:
                print("Buzz")
            else:
                print(i)

# Placeholder example use of the fizzBuzz() function
fizzBuzz(100)