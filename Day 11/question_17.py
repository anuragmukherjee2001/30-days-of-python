def factorial(number):
    fact = 1

    for i in range(2, number + 1):
        fact = fact * i

    return fact

print(factorial(5))        