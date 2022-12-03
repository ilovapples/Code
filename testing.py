import stats, random
numbers = []
for x in range(random.randint(2,15)):
    numbers.append(random.randint(1,150))
numbersStr = ""
index = 0
comma = ", "
for x in range(len(numbers)):
    if numbers[index] is not numbers[-1]:
        comma = ", "
    elif numbers[index] is numbers[-1]:
        comma = ""
    numbersStr += str(numbers[index]) + comma
    index += 1
print(numbersStr)
print("________________")
print("Average: " + str(stats.average(numbers)))
print("Median: " + str(stats.median(numbers)))
print("Mode: " + str(stats.mode(numbers)))