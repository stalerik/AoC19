import os

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
values = content.split(",")

for i in range(len(values)):
    values[i] = int(values[i])
current_instruction = 0
i = 0

while True:
    if values[i] == 99:
        break
    elif values[i] == 1:
        values[values[i+3]] = values[values[i+1]] + values[values[i+2]]
    elif values[i] == 2:
        values[values[i+3]] = values[values[i+1]] * values[values[i+2]]

    i += 4

print(values)
