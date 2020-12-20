def lists(ele):
    return ele * ele * ele 

lsts = [1, 2, 3, 4]
res = map(lists, lsts) 
print("The original list is: ") 
print(lsts)
print("The cube of the lists is: ")  
print(list(res))


# filter function

numbers = [1, 2, 3, 4, 5]

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))    

