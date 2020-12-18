import random

def list_of_rgb_colors(n):
    lst_of_col = []
    for i in range(n):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)

        col = "rgb({},{},{})".format(a,b,c)

        lst_of_col.append(col)
    return lst_of_col

n = int(input("Enter the number of colours you want: "))
print(list_of_rgb_colors(n))        
