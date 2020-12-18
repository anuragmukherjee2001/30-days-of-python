import random

def rgb_color_gen():
    a = random.randint(0, 255)
    b = random.randint(0, 255)
    c = random.randint(0, 255)
    # print("rgb(", a, ",",b, ",", c ,")")
    col = "rgb({},{},{})".format(a,b,c)
    print(col)

rgb_color_gen()    