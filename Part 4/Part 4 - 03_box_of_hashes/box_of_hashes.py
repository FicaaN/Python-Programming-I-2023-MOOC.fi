def line(length: int, text: str):
    if len(text) == 1:
        print(length * text)
    elif len(text) > 1:
        print(length * text[0])
    elif text == "":
        print(length * '*')

def box_of_hashes(height):
    for row in range(height):
        line(10, '#')

if __name__ == "__main__":
    box_of_hashes(5)