countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

two_dimentional = [number for row in countries for number in row]
one_dimentional = [number for row in two_dimentional for number in row]
print(one_dimentional)