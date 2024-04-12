def list_of_stars(list: list):
    for i in range(len(list)):
        number = list[i]
        print('*' * number)

if __name__ == "__main__":
    print(list_of_stars([3, 7, 1, 1, 2]))