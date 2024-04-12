def histogram(string: str):

    letters = {}

    for char in string:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1

    for letter, count in letters.items():
        print(f"{letter} {'*' * count}")

if __name__ == "__main__":

    histogram("abba")
    histogram("statistically")