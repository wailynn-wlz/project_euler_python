def is_prime_num(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    else:
        return True


prime_numbers = [i for i in xrange(2, 10000) if is_prime_num(i)]

for i in range(0,1000):
    if (prime_numbers[i] + prime_numbers[i + 1]) in prime_numbers:
        print prime_numbers[i]
