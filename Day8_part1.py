import os

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()

zeroes = 0
ones = 0
twos = 0

res = []

last = 0
for i in range(len(content)):
    if i % 25 == 0:
        line = content[last:i]
        print(line)
        for e in line:
            if e == '0':
                zeroes += 1
            elif e == '1':
                ones += 1
            elif e == '2':
                twos += 1

        last = i
        #h += 1
        if i % 150 == 0 and i != 0:
            print(zeroes, "------------", ones*twos)
            res.append((zeroes,ones*twos))
            zeroes = 0
            ones = 0
            twos = 0

smallest = 10000000000000000000
saved = 0
for e in res:
    if e[0] < smallest:
        smallest = e[0]
        saved = e

print(saved)
