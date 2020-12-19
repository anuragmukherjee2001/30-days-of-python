list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

two_dimentional = [number for row in list_of_lists for number in row]
one_dimentional = [number for row in two_dimentional for number in row]
print(one_dimentional)
