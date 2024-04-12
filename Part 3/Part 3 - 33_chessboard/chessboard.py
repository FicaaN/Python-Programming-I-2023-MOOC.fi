def chessboard(number):
    for i in range(number):
            for j in range(number):
                if (i + j) % 2 == 0:
                    print(1, end="")
                else:
                    print(0, end="")
            print()
if __name__ == "__main__":
    chessboard(3)