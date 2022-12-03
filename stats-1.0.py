def average(numbers):
    numbersIndex = 0
    averagedNumber = 0
    if isinstance(numbers, list):
        for x in range(len(numbers)):
            averagedNumber += numbers[numbersIndex]
            numbersIndex += 1
        averagedNumber /= len(numbers)
    return averagedNumber
def median(numbers):
    medianNumber = 0
    if len(numbers)%2 == 0:
        medianNumber = average([numbers[int(len(numbers)/2-1)], numbers[int(len(numbers)/2)]])
    else:
        medianNumber = numbers[int(len(numbers)/2-0.5)]
    return medianNumber
def mode(numbers):
    numbersIndex = 0
    counts = []
    countsSorted = None
    modeNumbers = None
    for x in range(len(numbers)):
        counts.append(numbers.count(numbers[numbersIndex]))
        numbersIndex += 1
    countsSorted = sorted(counts)
    modeNumbers = numbers[counts.index(countsSorted[-1])]
    return float(modeNumbers)