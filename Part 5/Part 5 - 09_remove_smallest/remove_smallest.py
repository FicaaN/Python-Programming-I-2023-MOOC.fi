def remove_smallest(numbers: list):

    min_number = numbers.index(min(numbers))

    numbers.pop(min_number)

if __name__ == "__main__":

    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)