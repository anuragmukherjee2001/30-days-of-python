fruits = ['banana', 'orange', 'mango', 'lemon']

inp = input("Enter the name of the fruit: ")

if inp not in fruits:
    fruits.append(inp)
    print(fruits)
else:
    print('That fruit already exist in the list')    
