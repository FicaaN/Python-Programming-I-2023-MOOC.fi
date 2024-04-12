def line(length: int, text: str):
    if len(text) == 1:
        print(length * text)
    elif len(text) > 1:
        print(length * text[0])
    elif text == "":
        print(length * '*')

def square(size, character):
    for row in range(size):
        line(size, character)

if __name__ == "__main__":
    square(5, "x")