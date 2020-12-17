import statistics

def calculate_mean(lst):
    sum_of_the_list = sum(lst)
    mean = sum_of_the_list/len(lst)
    return mean

def calculate_median(lst):
    if(len(lst) % 2 == 0):
        midean = (lst[len(lst) // 2] + lst[(len(lst) + 1) // 2]) / 2
    else:
        midean = lst[len(lst)//2]

    return midean

def calculate_mode(lst):
    return statistics.mode(lst) 

def calculate_variance(lst):
    return statistics.variance(lst) 

def calculate_std(lst):
    return statistics.stdev(lst)                  

lst = [1,2,3,4,5]

print(calculate_mean(lst))    
print(calculate_median(lst))    
print(calculate_mode(lst))
print(calculate_variance(lst))
print(calculate_std(lst))