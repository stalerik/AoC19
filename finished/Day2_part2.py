import os

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
input_values = content.split(",")

values = []
def reset_input(v):
    v = []
    for e in input_values:
        v.append(int(e))
    return v

current_instruction = 0
j = 0
k = 0
output = 0
while output != 19690720:
    values = reset_input(values)
    i = 0
    values[1] = k
    values[2] = j
    if k == 99:
        k = 0
        j += 1
        if j == 100:
            break
    while True:
        if values[i] == 99:
            break
        elif values[i] == 1:
            values[values[i+3]] = values[values[i+1]] + values[values[i+2]]
        elif values[i] == 2:
            values[values[i+3]] = values[values[i+1]] * values[values[i+2]]

        i += 4

    output = values[0]

    k += 1
print(values)
