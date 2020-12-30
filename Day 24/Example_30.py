import numpy as np

np_list_one = np.array([1, 2, 3])
np_list_two = np.array([4, 5, 6])

print(np_list_one + np_list_two)

print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))
