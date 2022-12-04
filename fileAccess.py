def accessFile(filename, text, readWriteAppend):
    if readWriteAppend.lower() == "write":
        write(filename, text)
    elif readWriteAppend.lower() == "read":
        print(read(filename))
    elif readWriteAppend.lower() == "append":
        append(filename, text)
def write(filename, text):
    with open(filename, "w") as fileObj:
        fileObj.write(text)
        
def read(filename):
    with open(filename, "r") as fileObj:
        return fileObj.read()
    
def append(filename, text):
    with open(filename, "a") as fileObj:
        fileObj.write(text)
while True:
    accessFile(input("Filename: "), input("Text input for Write or Append (input doesn't matter if reading): "), input("Read, Write, or Append: "))
