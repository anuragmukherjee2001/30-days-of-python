def add_item(lst, item):
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))    

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))