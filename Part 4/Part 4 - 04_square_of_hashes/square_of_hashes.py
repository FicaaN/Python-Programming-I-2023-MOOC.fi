def line(length: int, text: str):
    if len(text) == 1:
        print(length * text)
    elif len(text) > 1:
        print(length * text[0])
    elif text == "":
        print(length * '*')

def square_of_hashes(size):
    for row in range(size):
        line(size, "#")

if __name__ == "__main__":
    square_of_hashes(5)