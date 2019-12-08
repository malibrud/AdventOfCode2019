import numpy as np
import math

def isValidPW(n):
    s = str(n)
    lastVal = '0'
    digitsSame = False
    for c in s:
        if c == lastVal:
            digitsSame = True
        if c < lastVal:
            return False
        lastVal = c
    return digitsSame

fd = open('data.txt', 'r')
bounds = fd.readline().strip().split('-');
n1 = int(bounds[0])
n2 = int(bounds[1])

validPasswords = 0
for n in range(n1, n2+1):
    if isValidPW(n):
        validPasswords += 1

print(validPasswords)

