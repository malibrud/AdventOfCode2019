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

minDist = 1000000
for n in commonNodes:
    d1 = route1.index(n) + 1
    d2 = route2.index(n) + 1
    dist = d1 + d2;
    if dist < minDist:
        minDist = dist

print(minDist)

