import math


def count(n):
    result = 0
    for i in n:
        x = n.count(i)
        if x > result:
            result = i
    return result


arr = []
for a in range(1, 1000):
    for b in range(1, 1000):
        c = math.sqrt((a ** 2) + (b ** 2))
        p = a + b + c
        if p % 1 == 0 and p <= 1000:
            arr.append(p)
        else:
            continue


print count(arr)
