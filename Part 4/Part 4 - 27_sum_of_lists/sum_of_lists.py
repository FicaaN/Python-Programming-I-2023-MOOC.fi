def list_sum(list1: list, list2: list):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] + list2[i])
    return new_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))