def mean(list: list) -> float:
    sum_list = sum(list)
    length_list = len(list)
    return sum_list / length_list

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)