import numpy as np
import math

data = np.loadtxt('data.txt')
data = np.floor(data/3) - 2
sum = np.sum(data)
print(sum)
