def read_input(prompt: str, b1: int, b2: int) -> int:

    while True:
        try:
            number = int(input(prompt))
            if b1 <= number <= b2:
                return number
            else:
                print(f"You must type in an integer between {b1} and {b2}")
        except:
            print(f"You must type in an integer between {b1} and {b2}")

if __name__ == "__main__":

    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)