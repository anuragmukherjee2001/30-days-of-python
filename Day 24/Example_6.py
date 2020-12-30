import numpy as np

nums = np.array([1, 2, 3, 4, 5])
print(nums)

two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)

print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)

print('shape of numpy_two_dimensional_list: ',
      numpy_two_dimensional_list.shape)

three_by_four_array = np.array([[0, 1, 2, 3],
                                [4, 5, 6, 7],
                                [8, 9, 10, 11]])
print(three_by_four_array.shape)
