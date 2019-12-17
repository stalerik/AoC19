import os

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
values = content.split(",")

for i in range(len(values)):
    values[i] = int(values[i])
current_instruction = 0
adress = 0


jumped = False
while True:
    temp = str(values[adress])
    if len(temp) <3:
        opcode = int(temp)
        mode_first = 0
        mode_second = 0
        mode_third = 0

    elif len(temp) == 3:
        opcode = int(temp[1::])
        mode_first = 1
        mode_second = 0
        mode_third = 0

    elif len(temp) == 4:
        opcode = int(temp[2::])
        mode_first = int(temp[1])
        mode_second = int(temp[0])
        mode_third = 0
    else:
        opcode = int(temp[3::])
        mode_first = int(temp[2])
        mode_second = int(temp[1])
        mode_third = int(temp[0])


    #print("adress:", adress, "opcode:", opcode)


    #Detta är ju typ helt fel
    if mode_first == 0:
        first_param = values[values[adress+1]]
    elif mode_first == 1:
        first_param = values[adress+1]
    if opcode < 3 or opcode > 4:
        if mode_second == 0:
            second_param = values[values[adress+2]]
        elif mode_second == 1:
            second_param = values[adress+2]

    third_param = values[adress + 3]
    """if opcode > 6:
        if mode_third == 0:
            third_param = values[adress + 3]
        elif mode_third == 1:
            third_param = values[adress + 3]
"""
    #print("first:",first_param, "second:",second_param, "third:", third_param)
    #print("Vfirst:", values[first_param], "vsecond:",values[second_param], "vthird:", values[third_param])



    if opcode == 99:
        break

    elif opcode == 1:
        #print("value param 3:", values[values[adress+3]])
        #print("sum:", first_param + second_param)
        #print("first param:",first_param, "second_param:", second_param)
        values[values[adress+3]] = first_param + second_param

    elif opcode == 2:
        values[values[adress+3]] = first_param*second_param

    elif opcode == 3:
        input1 = int(input("opcode is 3: "))
        #special case. always imidiate mode here
        values[values[adress + 1]] = input1

    elif opcode == 4:
        print("value at address", values[adress + 1], "is:", first_param)

    elif opcode == 5:
        #print("first_param:",first_param)
        if first_param != 0:
            adress = second_param
            jumped = True

    elif opcode == 6:
        if first_param == 0:
            adress = second_param
            jumped = True

    elif opcode == 7:
        if first_param < second_param:
            values[third_param] = 1
        else:
            values[third_param] = 0

    elif opcode == 8:
        #print(third_param)
        if first_param == second_param:

            values[third_param] = 1
        else:
            values[third_param] = 0

    if opcode < 3 or opcode > 6:
        adress += 4

    elif ((opcode == 5 or opcode == 6) and not jumped):
        adress += 3

    elif opcode == 3 or opcode == 4:
        adress += 2
    jumped = False

    #print(values)
