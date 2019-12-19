def computeTransfers(input):
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

    # get 'YOU' chain
    p = 'YOU'
    youChain = []
    while True:
        youChain.append(p)
        if p in tree:
            p = tree[p]
        else:
            break
    youChain.reverse()
    #print(youChain)
    
    # get 'SAN' chain
    p = 'SAN'
    sanChain = []
    while True:
        sanChain.append(p)
        if p in tree:
            p = tree[p]
        else:
            break
    sanChain.reverse()
    #print(sanChain)

    commonDepth = 0
    for i in range(len(sanChain)):
        if youChain[i] != sanChain[i]:
            break
        else:
            commonDepth += 1
    result = len(youChain) - commonDepth - 1 + len(sanChain) - commonDepth - 1
    return result

testData = open('testB.txt', 'r').read()
result = computeTransfers(testData)
print(f'Test 1: {result}')

data = open('data.txt', 'r').read()
result = computeTransfers(data)
print(f'Result: {result}')