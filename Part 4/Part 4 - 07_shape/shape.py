def line(length: int, text: str):
    if len(text) == 1:
        print(length * text)
    elif len(text) > 1:
        print(length * text[0])
    elif text == "":
        print(length * '*')

def shape(one, two, three, four):
    for row in range(1, one + 1):
        line(row, two)
    for row1 in range(three):
        line(one, four)
        
if __name__ == "__main__":
    shape(5, "x", 2, "o")