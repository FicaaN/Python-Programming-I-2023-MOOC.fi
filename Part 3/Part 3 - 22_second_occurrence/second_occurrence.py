string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

if substring in string:
    index = string.find(substring)
    length = len(substring)
    string1 = string[index + length:]
    add = len(string) - len(string1)

    if substring in string1:
        index1 = add + string1.find(substring)
        print(f"The second occurrence of the substring is at index {index1}.")
    else:
        print("The substring does not occur twice in the string.")
else:
    print("The substring does not occur twice in the string.")