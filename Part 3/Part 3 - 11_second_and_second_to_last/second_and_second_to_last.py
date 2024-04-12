string = input("Please type in a string: ")

sec = string[1]
sec_to_last = string[-2]

if sec == sec_to_last:
    print(f"The second and the second to last characters are {sec}")
else:
    print("The second and the second to last characters are different")