def spruce(size):
    print("a spruce!")
    for row in range(size):
        spaces = size - row - 1
        stars = 2 * row + 1

        print(" " * spaces + "*" * stars + " " * spaces)

    print(" " * (size - 1) + "*")

if __name__ == "__main__":
    spruce(5)