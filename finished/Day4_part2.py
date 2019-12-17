import os


file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
range_numbers = content.split("-")

low = int(range_numbers[0])
high = int(range_numbers[1])

def inc_number(number):
    for i in range(len(number)):
        for j in range(i,len(number)):
            if int(number[j]) < int(number[i]):
                return False
    return True

def large_group(number):
    last = ''
    has_large = False
    has_two = False
    c= 1
    last = number[0]
    for i in range(1,len(number)):
        if number[i] == last:
            c += 1
        elif number[i] != last:
            if c == 2:

                return True
            else:
                last = number[i]
                c = 1
    #Edge case for last number
    if c == 2:
        return True
    else:
        return False


counter = 0
for i in range(low, high):
    number = str(i)
    #makes sure there is two of a number and it increases
    if len(set(number)) < 6 and inc_number(str(i)):
        if (large_group(str(i))):

            counter += 1

print(counter)
