empty_tuple = ()

brother_tuples = ('Priyodarshan', 'Davis', 'Priyanshu')
sister_tuples = ('Elisa', 'Dia', 'Emma')

siblings = brother_tuples + sister_tuples

print(len(siblings))

family_members = siblings +  ('My_father', 'My_mother')
print(family_members)

parents_unpacked = family_members[6:8]
siblings_unpacked = family_members[0:6]

fruits = ['Mango', 'Guava', 'orange']
vegetables = ['Brinjal', 'Potato', 'Onion']
animal_products = ['Milk', 'Meat', 'Egg']

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

food_stuff_lt = []
food_stuff_lt = food_stuff_tp
print(food_stuff_lt)

print(food_stuff_tp[len(food_stuff_tp)//2:len(food_stuff_tp)//2 + 1])

print(food_stuff_tp[0:3])
print(food_stuff_tp[len(food_stuff_tp) - 3:len(food_stuff_tp)])

del food_stuff_tp


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Estonia' in nordic_countries:
    print("True")
else:
    print("False")    

if 'Iceland' in nordic_countries:
    print("True")
else:
    print("False")