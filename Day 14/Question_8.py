numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(n):
    return n * n

res = map(square, numbers)
print(list(res))    