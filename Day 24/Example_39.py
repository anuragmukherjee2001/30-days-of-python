import numpy as np

four_by_four_matrix = np.matrix(np.ones((4, 4), dtype=float))
np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)
