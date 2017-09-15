pentagonal = [n*(3 * n - 1)/2 for n in range(1000,10000)]

for i in pentagonal:
    for j in pentagonal:
        if (i + j) in pentagonal and (j - i) in pentagonal:
            print i,j,' and result is ', j - i
            break
