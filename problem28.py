total = 1
num = 1

for index in range(2,1001,2):
    for reps in range(4):
        num += index
        print num
        total += num


print total
