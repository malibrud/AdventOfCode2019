def computeOrbits(input):
    lines = input.splitlines()
    tree = {}
    all = []
    for line in lines:
        planets = line.split(')')
        inner = planets[0]
        outer = planets[1]
        all.append(inner)
        all.append(outer)
        if outer not in tree:
            tree[outer] = inner
    all = list(set(all))
    result = 0
    for planet in all:
        p = planet
        depth = 0
        while True:
            if p in tree:
                p = tree[p]
                depth += 1
            else:
                break
        #print(f'Planet: {planet}, depth: {depth}')
        result += depth

    #print(all)
    #print(tree)
    return result

testData = open('test.txt', 'r').read()
result = computeOrbits(testData)
print(f'Test 1: {result}')

data = open('data.txt', 'r').read()
result = computeOrbits(data)
print(f'Result: {result}')