def print_sudoku(sudoku):
    
    for i in range(9):
        if i % 3 == 0:
            print()
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("", end=" ")
            if sudoku[i][j] == 0:
                print("_", end=" ")
            else:
                print(sudoku[i][j], end=" ")
        print()

def add_number(sudoku, row_no, column_no, number):

    sudoku[row_no][column_no] = number

if __name__ == "__main__":

    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print("Initial Sudoku:")
    print_sudoku(sudoku)

    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)

    print("\nThree numbers added:")
    print_sudoku(sudoku)