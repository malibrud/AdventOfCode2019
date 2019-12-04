import numpy as np
import math

data = np.loadtxt('data.txt', delimiter=',')

data[1] = 12
data[2] = 2

pc = 0
while True:
    opcode = data[pc]
    if opcode == 1:
        a = int(data[pc+1])
        b = int(data[pc+2])
        c = int(data[pc+3])
        data[c] = data[a] + data[b]
    if opcode == 2:
        a = int(data[pc+1])
        b = int(data[pc+2])
        c = int(data[pc+3])
        data[c] = data[a] * data[b]
    if opcode == 99:
        break
    pc = pc + 4

print(data[0])
