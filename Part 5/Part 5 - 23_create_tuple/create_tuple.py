def create_tuple(x: int, y: int, z: int):
    
    min_number = min(x, y, z)
    max_number = max(x, y, z)
    sum_numbers = x + y + z

    tuple = (min_number, max_number, sum_numbers)

    return tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))