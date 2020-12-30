import numpy as np

h = [[1, 2], [3, 4]]
i = [[5, 6], [7, 8]]
res = np.matmul(h, i)
print(res)

res2 = np.linalg.det(i)
print(res2)
