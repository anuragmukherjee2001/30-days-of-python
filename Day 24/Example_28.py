import numpy as np

first_shape = np.array([(1, 2, 3), (4, 5, 6)])
print(first_shape)
reshaped = first_shape.reshape(3, 2)
print(reshaped)
