first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

if first <= second <= third or third <= second <= first:
    print(f"The letter in the middle is {second}")
elif second <= first <= third or third <= first <= second:
    print(f"The letter in the middle is {first}")
else:
    print(f"The letter in the middle is {third}")