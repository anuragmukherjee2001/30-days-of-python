import math

my_age:int = 19
my_height:float = 5.8

complex_var:complex = 4 + 4j

base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height

print("The area of the triangle is ", int(area))

sideA = int(input("Enter the side a: "))
sideB = int(input("Enter the side b: "))
sideC = int(input("Enter the side c: "))

perimeter = sideA + sideB + sideC

print("The perimeter of the triangle is ",perimeter)

length_rect = int(input("Enter the length: "))
width_rect = int(input("Enter the width: "))

area_rect = length_rect * width_rect
perimeter_rect = 2 * (length_rect * width_rect)

print("The area of the rectangle is: ", area_rect)
print("The perimeter of the rectangle is: ", perimeter_rect)

radius = int(input("Enter the radius of the circle: "))

area_circle = math.pi * radius * radius
circumference = 2 * math.pi * radius

print("The area of the circle is: ", area_circle)
print("The circumference of the circle is: ", circumference)

x1, x2, y1, y2 = 2, 6, 2, 10

slope = (y2 - y1)/(x2 - x1)
print("The slope is: ",slope)

x = int(input("Enter the value of x: "))
y = x * x + 6 * x + 9
print("The value of y is: ", y)

# x = -3, when y = 0

str1 = "python"
str2 = "jargon"

if str1 == str2:
    print("True")
else:
    print("False")

str3 = "I hope this course is not full of jargon"
if 'jargon' in str3:
    print("The string is present")
else:
    print("The string is not present")    

str4 = "dragon"
str5 = "python"

if 'on' not in str4 and str5:
    print('There is no on in dragon and python')

else:
    print("On is present in dragon and python") 

str6 = "python"
len_str6 = float(len(str6))
len_str6_tostring = str(len(str6))
print(len_str6)       
print(len_str6_tostring)       

num = int(input("Enter the number: "))

if num % 2 == 0:
    print("The number is even")

else:
    print("The number is odd")    

print(int(7//3))

if type('10') == type(10):
    print("True")

else:
    print("False") 
   
a = '9.8'
int_a = int(a)

if int_a == 10:
    print("True")

else:
    print("False")   

# Gives an error     

hours = int(input("Enter hours: "))
rate_per_hours = int(input("Enter rate per hour: "))
earnimg = hours * rate_per_hours

print("Your weekly earning is", earnimg)

years = int(input("Enter number of years you have lived: "))

seconds_lived = years * 365 * 24 * 60 * 60
print("You have lived for ",seconds_lived, "seconds")

print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)