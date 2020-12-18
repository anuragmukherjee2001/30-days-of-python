import random

def unique_random_numbers():
    lst = []
    lst = random.sample(range(0,9),7)
    return lst

print(unique_random_numbers())    