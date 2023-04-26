def combine(str_arr: list, seperate: str):
    final = ""
    for i in str_arr:
        if not i is str_arr[-1]:
            final += i + seperate
        else:
            final += i
    return final

if __name__ == "__main__":
    string = "Hello World! This is a String!"
    f = string.split(" ")
    print(f"String After Splitting: {str(f)}")
    string = combine(f, "|")
    print(f"String After Combining: {str(string)}")