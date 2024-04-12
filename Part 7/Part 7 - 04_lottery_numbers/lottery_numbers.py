import random

def lottery_numbers(amount: int, lower: int, upper: int):

    if lower >= upper:
        raise ValueError("Upper bound must be greater then lower bound")
    
    lottery_list = random.sample(range(lower, upper + 1), min(amount, upper - lower + 1))

    lottery_list.sort()

    return lottery_list

if __name__ == "__main__":

    for number in lottery_numbers(7, 1, 40):
        print(number)