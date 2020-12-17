sumEven = 0
sumOdd = 0

for i in range(0, 101):
    if(i % 2 == 0):
        sumEven = sumEven + i

    else:
        sumOdd += i

print("The sum of all even is ", sumEven)            
print("The sum of all odd is ", sumOdd)            