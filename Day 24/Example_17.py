import numpy as np

numpy_int_arr = np.array([1, 2, 3, 4], dtype='float')
print(numpy_int_arr)

numpy_int_arr = np.array([1., 2., 3., 4.], dtype='int')
print(numpy_int_arr)

numpy_float_arr = numpy_int_arr.astype('int').astype('str')
print(numpy_float_arr)
