import random

def roll(die: str):

    if die == "A":
        return random.choice([3, 3, 3, 3, 3, 6])
    elif die == "B":
        return random.choice([2, 2, 2, 5, 5, 5])
    elif die == "C":
        return random.choice([1, 4, 4, 4, 4, 4])
    else:
        raise ValueError("Invalid die")
    
def play(die1: str, die2: str, times: int):

    win_die1 = 0
    win_die2 = 0
    ties = 0

    for _ in range(times):
        roll_die1 = roll(die1)
        roll_die2 = roll(die2)

        if roll_die1 > roll_die2:
            win_die1 += 1
        elif roll_die2 > roll_die1:
            win_die2 += 1
        else:
            ties += 1

    return win_die1, win_die2, ties

if __name__ == "__main__":

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)