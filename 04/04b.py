import numpy as np
import math

def isValidPW(n):
    s = str(n)
    # check for monotonicity
    lastVal = '0'
    for c in s:
        if c < lastVal:
            return False
        lastVal = c

    # check for a run of 2
    for c in range(ord('0'), ord('9')+1):
        if s.count(chr(c)) == 2:
            return True
    return False

fd = open('data.txt', 'r')
bounds = fd.readline().strip().split('-');
n1 = int(bounds[0])
n2 = int(bounds[1])

validPasswords = 0
for n in range(n1, n2+1):
    if isValidPW(n):
        validPasswords += 1
        print(n)

print(validPasswords)

