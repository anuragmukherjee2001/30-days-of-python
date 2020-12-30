import numpy as np

two_dimension_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(two_dimension_array)
two_dimension_array[1, 1] = 55
two_dimension_array[1, 2] = 44
print(two_dimension_array)
