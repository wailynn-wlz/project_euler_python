n = 99999


def f(num):
    return sorted(str(num))


while not f(n * 2) == f(n * 3) == f(n * 4) == f(n * 5) == f(n * 6):
    n += 9

print n
