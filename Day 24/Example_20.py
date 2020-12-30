import numpy as np

two_dimension_array = np.array([[0, 1, 2],
                                [3, 4, 5],
                                [6, 7, 8]])

first_column = two_dimension_array[:, 0]
second_column = two_dimension_array[:, 1]
third_column = two_dimension_array[:, 2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)
