names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

two_dimentional = [number for row in names for number in row]
one_dimentional = [number for row in two_dimentional for number in row]
print(one_dimentional)