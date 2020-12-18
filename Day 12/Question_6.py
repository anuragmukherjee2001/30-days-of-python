import random

def list_of_rgb_colors(n):
    lst_of_col = []
    for i in range(n):
        a = random.randint(0, 255)
        b = random.randint(0, 255)
        c = random.randint(0, 255)

        col = "rgb({},{},{})".format(a,b,c)

        lst_of_col.append(col)
    print(lst_of_col)

def list_of_hexa_colors(n):
    lst_of_col = []
    hexa = '0123456789ABCDEF'
    for i in range(n):
        result_color = '#'+''.join(random.choice(hexa) for i in range(6))
        lst_of_col.append(result_color)
    print(lst_of_col)

def generate_colors(col, n):
    if col == 'hexa':
        list_of_hexa_colors(n)
    elif col == 'rgb':
        list_of_rgb_colors(n) 
    else:
        print("Please enter a valied input")


col = input("Enter the type of colours: ")
n = int(input("Enter the number of colours: "))

generate_colors(col, n)