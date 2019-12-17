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


counter = 0
for i in range(low, high):
    number = str(i)
    if len(set(number)) < 6 and inc_number(str(i)): #makes sure there is two of a number and it increases
        counter += 1

print(counter)
