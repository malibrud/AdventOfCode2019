import numpy as np
import math

def getFuel(mass):
    m = mass
    f = 0
    while True:
        m = fuel = np.floor(m/3) - 2
        if m <= 0:
            break
        f = f + fuel
    return f

data = np.loadtxt('data.txt')

sum = 0
for mass in np.nditer(data):
    f = getFuel(mass)
    sum = sum + f

print(sum)

