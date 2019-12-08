import numpy as np
import math

def parseSegment(w):
    if w[0] == 'L':
        dx = -1
        dy =  0
    if w[0] == 'R':
        dx = +1
        dy =  0
    if w[0] == 'D':
        dx =  0
        dy = -1
    if w[0] == 'U':
        dx =  0
        dy = +1
    d = int(w[1:])
    return (dx, dy, d)

def getWireCoordinates(wireList):
    x = y = 0
    N = len(wireList)
    coords = []
    for w in wireList:
        (dx, dy, d) = parseSegment(w)
        for i in range(d):
            x = x + dx
            y = y + dy
            coords.append((x, y))
    return coords

fd = open('data.txt', 'r')
line1 = fd.readline().strip()
line2 = fd.readline().strip()

wire1 = line1.split(',');
wire2 = line2.split(',');
route1 = getWireCoordinates(wire1)
route2 = getWireCoordinates(wire2)

commonNodes = set(route1) & set(route2)
distList = list(map(lambda x: abs(x[0]) + abs(x[1]), commonNodes))
print(min(distList))

