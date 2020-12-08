# Exercise level 1

# Day 2: 30 Days of python programming

first_name = "Anurag"
last_name = "Mukherjee"
full_name ="Anurag Mukherjee"
country = "India"
city = "Kolkata"
age = 19
year = 2020
is_married = False
is_true = True
is_light_on = False
x, y, z = 10, 16, 20

# Exercise Level 2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(x))
print(type(y))
print(type(z))

# finding the length of the first name using builf in functions

print(len(first_name))

# comparing the length of the last name and the first name

if (len(first_name) == len(last_name)):
    print("They are similar")
else:
    print("They are not similar")    

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_the_circle = 3.14 * radius * radius
circum_of_the_circle = 2 * 3.14 * radius

radius = input("Enter the radius of the circle")
area_of_the_circle = 3.14 * radius * radius

first_name = input("Enter the first name")
last_name = input("Enter the last name")
country = input("Enter the country")
age = input("Enter the age")