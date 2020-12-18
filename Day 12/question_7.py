import random

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

lst = [1,5,6,9,10]
print(shuffle_list(lst))    