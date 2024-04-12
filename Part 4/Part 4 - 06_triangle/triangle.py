def line(length: int, text: str):
    if len(text) == 1:
        print(length * text)
    elif len(text) > 1:
        print(length * text[0])
    elif text == "":
        print(length * '*')

def triangle(size):
    for row in range(1, size + 1):
        line(row, "#")

if __name__ == "__main__":
    triangle(5)