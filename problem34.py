import math

sum = 0

for num in range(3,50000):
    digits_factorial_sum = 0
    for digit in str(num):
        digits_factorial_sum += math.factorial(int(digit))
    if digits_factorial_sum == num:
        sum += num
        print num
