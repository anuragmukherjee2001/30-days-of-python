from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def add(num1, num2):
    return num1 + num2


total = reduce(add, numbers)
print(total)    