def sum_of_numbers(num_range):
    sum_all = 0
    for i in range(0, num_range + 1):
        sum_all += i

    return sum_all

print(sum_of_numbers(100))        
print(sum_of_numbers(10))        
print(sum_of_numbers(5))        