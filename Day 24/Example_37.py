import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

normal_array = np.random.normal(79, 15, 80)
normal_array

sns.set()
plt.hist(normal_array, color="grey", bins=50)
