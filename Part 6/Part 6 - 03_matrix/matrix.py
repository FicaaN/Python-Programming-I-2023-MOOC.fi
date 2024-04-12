def read_matrix():
    matrix = []

    with open("matrix.txt") as file:
        
        for line in file:
            row = [int(value) for value in line.strip().split(',')]
            matrix.append(row)
        
    return matrix

def matrix_sum():
    matrix = read_matrix()

    sum_total = sum(sum(row) for row in matrix)

    return sum_total

def matrix_max():
    matrix = read_matrix()

    element_max = max(max(row) for row in matrix)

    return element_max

def row_sums():
    matrix = read_matrix()

    row_sums_list = [sum(row) for row in matrix]
    
    return row_sums_list

if __name__ == "__main__":
    pass