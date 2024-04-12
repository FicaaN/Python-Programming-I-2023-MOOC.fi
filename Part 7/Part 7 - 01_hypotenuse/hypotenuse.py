import math

def hypotenuse(leg1: float, leg2: float):

    c = (leg1 * leg1) + (leg2 * leg2)

    hypo = math.sqrt(c)

    return hypo

if __name__ == "__main__":

    print(hypotenuse(3,4)) # 5.0
    print(hypotenuse(5,12)) # 13.0
    print(hypotenuse(1,1)) # 1.4142135623730951