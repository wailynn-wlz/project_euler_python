triangles = [n*(n + 1)/2 for n in range(286,100000)]
pentagonal = [n*(3 * n - 1)/2 for n in range(164,100000)]
hexagons = [n*(2 * n - 1) for n in range(143,100000)]

for i in triangles:
    if i in pentagonal and i in hexagons:
        print i
        break
