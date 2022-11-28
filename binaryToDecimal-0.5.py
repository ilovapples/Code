binaryInput = None
binaryInputIndexing = -1  # Indexing for the input
decimalOutput = 0  # Final output
decimalOutputAdditionCTRL = 1  # Amount to add to the final output


def checkBinChr():  # Define the function to check binaryInput for 1s
    binaryInput = input("Binary: ")  # Asks for binary input
    decimalOutput: int = 0
    binaryInputIndexing: int = -1
    decimalOutputAdditionCTRL: int = 1
    for x in range(len(binaryInput)):
        if binaryInput[binaryInputIndexing] == 1:
            decimalOutput += decimalOutputAdditionCTRL
        decimalOutputAdditionCTRL *= 2
        binaryInputIndexing -= 1
    print(decimalOutput)

checkBinChr()
