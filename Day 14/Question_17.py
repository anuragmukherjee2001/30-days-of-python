from functools import reduce
from operator import add

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

print (reduce(add,['Estonia ',',', ' Finland ',',', ' Sweden ',',', ' Denmark ',',', ' Norway ',',', ' Iceland ', 'are north European countries']))    