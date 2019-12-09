import os
import copy as cp

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
val = content.split(",")

for i in range(len(val)):
    val[i] = int(val[i])

adress_map = dict()

def run_int_code(values, inp, machine_letter, phase_bool):
    input_counter = 0
    adress = adress_map[machine_letter]
    jumped = False
    while True:
        temp = str(values[adress])
        if len(temp) < 3:
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
        #feedback loop solution
        if opcode == 99:
            #Vad ska göras här?
            #print("Machine:", machine_letter, "halted.")
            return -2



        if mode_first == 0:
            first_param = values[values[adress+1]]
        elif mode_first == 1:
            first_param = values[adress+1]
        if opcode < 3 or opcode > 4:
            if mode_second == 0:
                second_param = values[values[adress+2]]
            elif mode_second == 1:
                second_param = values[adress+2]

        if (len(values)) > adress+3:
            third_param = values[adress + 3]


        if opcode == 1:
            values[values[adress+3]] = first_param + second_param

        elif opcode == 2:
            values[values[adress+3]] = first_param*second_param

        elif opcode == 3:
            input_counter += 1
            #input1 = int(input("opcode is 3: "))
            #special case. always imidiate mode here
            #if set_phase and input_counter == 1:
            #    input1 = phase
            #else:
            #    input1 = inp
            #print(machine_letter, inp)
            if phase_bool and input_counter == 1:
                values[values[adress + 1]] = inp[1]
            else:
                values[values[adress+1]] = inp[0]

        #ouput followed imideately by 99 is halt
        elif opcode == 4:
            #print("value at address", values[adress + 1], "is:", first_param)
            #print(values[adress+2])
            #if values[adress+2] != 99:
            #print(machine_letter, first_param)
            adress_map[machine_letter] = adress +2
            return first_param
            #, adress+2, values[adress+2])
            #else:
            #    return (-2,-2,-2)

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


#Phases
A = 5
B = 5
C = 5
D = 5
E = 5

def inc_phase(A,B,C,D,E):
    if E == 10:
        D += 1
        E = 5
    if D == 10:
        C += 1
        D = 5
    if C == 10:
        B += 1
        C = 5
    if B == 10:
        A += 1
        B = 5
    return A,B,C,D,E

def check_if_halt(res):
    if res == -1:
        return True
    else:
        return False




amp_signals = []


while A != 10:
    prog_A = cp.copy(val)
    prog_B = cp.copy(val)
    prog_C = cp.copy(val)
    prog_D = cp.copy(val)
    prog_E = cp.copy(val)

    adress_map['A'] = 0
    adress_map['B'] = 0
    adress_map['C'] = 0
    adress_map['D'] = 0
    adress_map['E'] = 0

    if len(set([A,B,C,D,E])) == 5:
        result = 0
        phase = True
        r = 0
        while result != -2:
            if phase:
                result = run_int_code(prog_A, [result, A], 'A', phase)
                result = run_int_code(prog_B, [result, B], 'B', phase)
                result = run_int_code(prog_C, [result, C], 'C', phase)
                result = run_int_code(prog_D, [result, D], 'D', phase)
                result = run_int_code(prog_E, [result, E], 'E', phase)
                phase = False
            else:
                result = run_int_code(prog_A, [result], 'A', phase)
                result = run_int_code(prog_B, [result], 'B', phase)
                result = run_int_code(prog_C, [result], 'C', phase)
                result = run_int_code(prog_D, [result], 'D', phase)
                result = run_int_code(prog_E, [result], 'E', phase)
            if result != -2:
                r = result

    if len(set([A,B,C,D,E])) == 5:
        amp_signals.append((r,A,B,C,D,E))
    E += 1
    A,B,C,D,E = inc_phase(A,B,C,D,E)

biggest = 0
saved = 0

for e in amp_signals:
    if e[0] > biggest:
        biggest = e[0]
        saved = e
print(saved)
