import random

def list_of_hexa_colors(n):
    lst_of_col = []
    hexa = '0123456789ABCDEF'
    for i in range(n):
        result_color = '#'+''.join(random.choice(hexa) for i in range(6))
        lst_of_col.append(result_color)
    return lst_of_col


n = int(input("Enter the number of colours you want: "))
print(list_of_hexa_colors(n))        
