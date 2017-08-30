
result = []
for a in xrange(2,101):
    for b in range(2,101):
        result.append(a ** b)

terms = sorted(set(result))
print (len(terms))

