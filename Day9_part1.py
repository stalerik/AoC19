import os

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
values = content.split(",")
test = dict()
for i in range(len(values)):
    values[i] = int(values[i])
    test[i] = int(values[i])
#for i in range(100000):
#    values.append(0)

current_instruction = 0
adress = 0
relative_base = 0

jumped = False

def read_test(addr):
    if addr in test.keys():
        return(test[addr])
    else:
        return 0

while True:
    temp = str(read_test(adress))
    if len(temp) < 3:
        opcode = int(temp)
        mode_first = 0
        mode_second = 0
        mode_third = 1

    elif len(temp) == 3:
        opcode = int(temp[1::])
        mode_first = int(temp[0])
        mode_second = 0
        mode_third = 1

    elif len(temp) == 4:
        opcode = int(temp[2::])
        mode_first = int(temp[1])
        mode_second = int(temp[0])
        mode_third = 1
    else:
        opcode = int(temp[3::])
        mode_first = int(temp[2])
        mode_second = int(temp[1])
        mode_third = int(temp[0])


    #print(relative_base)
    #print(read_test(1000))
    #print("adress:", adress, "opcode:", opcode)

    if opcode == 99:
        break

    if mode_first == 0:
        first_param = read_test(read_test(adress+1))
    elif mode_first == 1:
        first_param = read_test(adress+1)
    elif mode_first == 2:
        first_param =  read_test(relative_base + read_test(adress+1))


    #if opcode < 3 or opcode > 4 and opcode < 9:
    if mode_second == 0:
        second_param = read_test(read_test(adress+2))
    elif mode_second == 1:
        second_param = read_test(adress+2)
    elif mode_second == 2:
        second_param = read_test(relative_base + read_test(adress +2))

    #if adress + 3 < len(read_test):
    if mode_third == 0:
        third_param = read_test(read_test(adress+3))
    elif mode_third == 1:
        third_param = read_test(adress+3)
    elif mode_third == 2:
        third_param = read_test(relative_base + read_test(adress +3))

    #third_param = test[adress + 3]




    if opcode == 1:
        #print("value param 3:", test[adress+3])
        #print("sum:", first_param + second_param)
        #print("first param:",first_param, "second_param:", second_param)
        if mode_third != 2:
            test[third_param] = first_param + second_param
        else:
            test[relative_base + read_test(adress + 3)] = first_param + second_param
    elif opcode == 2:
        if mode_third != 2:
            test[third_param] = first_param*second_param
        else:
            test[relative_base + read_test(adress + 3)] = first_param * second_param
    elif opcode == 3:
        input1 = int(input("opcode is 3: "))
        #special case. always imidiate mode here
        if mode_first != 2:
            test[read_test(adress + 1)] = input1
        else:
            test[relative_base + read_test(adress + 1)] = input1
        #print(relative_base, read_test(adress+1))
        #print(first_param)
        #print(read_test(1000))
        #test[first_param] = input1

    elif opcode == 4:
        #print("value at address", adress + 1 , "is:", first_param)
        print("value:",first_param)
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
        #print(first_param, second_param, third_param)
        if mode_third != 2:
            if first_param < second_param:
                test[third_param] = 1
            else:
                test[third_param] = 0
        else:
            if first_param < second_param:
                test[relative_base + read_test(adress + 3)] = 1
            else:
                test[relative_base  + read_test(adress +3)] = 0

    elif opcode == 8:
        #print(third_param)
        if mode_third != 2:
            if first_param == second_param:
                test[third_param] = 1
            else:
                test[third_param] = 0
        else:
            if first_param == second_param:
                test[relative_base + read_test(adress + 3)] = 1
            else:
                test[relative_base + read_test(adress + 3)] = 0

    elif opcode == 9:
        relative_base += first_param

    if opcode < 3 or opcode > 6 and opcode < 9:
        adress += 4

    elif ((opcode == 5 or opcode == 6) and not jumped):
        adress += 3

    elif opcode == 3 or opcode == 4 or opcode == 9:
        adress += 2
    jumped = False

    #print(test)
