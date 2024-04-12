from fractions import Fraction

def fractionate(amount: int):

    fraction_size = Fraction(1, amount)

    fraction_list = [fraction_size] * amount

    return fraction_list

if __name__ == "__main__":

    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))