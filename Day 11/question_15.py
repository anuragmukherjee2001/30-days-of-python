def sum_of_odds(num_range):
    sum_all = 0
    for i in range(0, num_range + 1):
        if i % 2 == 0:
            sum_all += i
    return sum_all

print(sum_of_odds(100))            