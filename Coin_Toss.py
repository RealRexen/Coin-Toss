import random

def coinToss():
    return random.randint(1, 3)

result = coinToss()
if result == 1:
    print("Its heads.")
if result == 2:
    print("Its Tails.")
if result == 3:
    print("It landed on its side!")
