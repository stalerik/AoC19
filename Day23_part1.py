import os
import copy as cp
import time

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
values = content.split(",")

val = dict()
for i in range(len(values)):
    val[i] = int(values[i])

current_instruction = 0
adress = 0
relative_base = 0

jumped = False

def read_test(addr, test):
    if addr in test.keys():
        return(test[addr])
    else:
        return 0


def run_int_code(inp, test, adr, machine, input_buffer):
	adress = adr[machine]
	global relative_base
	counter = 0
	inp_counter = 0
	while True:
	    temp = str(read_test(adress, test))
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
	    #print("adress:", adress, "opcode:", opcode, "machine#", machine)

	    if opcode == 99:
	        print("Halted")
	        return -1

	    if mode_first == 0:
	        first_param = read_test(read_test(adress+1, test),test)
	    elif mode_first == 1:
	        first_param = read_test(adress+1, test)
	    elif mode_first == 2:
	        first_param =  read_test(relative_base + read_test(adress+1,test), test)


	    #if opcode < 3 or opcode > 4 and opcode < 9:
	    if mode_second == 0:
	        second_param = read_test(read_test(adress+2, test),test)
	    elif mode_second == 1:
	        second_param = read_test(adress+2, test)
	    elif mode_second == 2:
	        second_param = read_test(relative_base + read_test(adress +2,test), test)

	    #if adress + 3 < len(read_test):
	    if mode_third == 0:
	        third_param = read_test(read_test(adress+3, test),test)
	    elif mode_third == 1:
	        third_param = read_test(adress+3,test)
	    elif mode_third == 2:
	        third_param = read_test(relative_base + read_test(adress +3,test), test)

	    #third_param = test[adress + 3]




	    if opcode == 1:
	        #print("value param 3:", test[adress+3])
	        #print("sum:", first_param + second_param)
	        #print("first param:",first_param, "second_param:", second_param)
	        if mode_third != 2:
	            test[third_param] = first_param + second_param
	        else:
	            test[relative_base + read_test(adress + 3, test)] = first_param + second_param
	    elif opcode == 2:
	        if mode_third != 2:
	            test[third_param] = first_param*second_param
	        else:
	            test[relative_base + read_test(adress + 3, test)] = first_param * second_param
	    elif opcode == 3:
	        #inp = int(input("opcode is 3: "))
	        #special case. always imidiate mode here
	        if machine == 27:
	        	print("input:",inp)
	        inf_loop = False
	        if not inp: #After initial
	        	adress_map[machine] = adress +2
	        	return -1, -1,- 1
	        if inp == [-1]:
	        	inf_loop = True
	        if mode_first != 2:
	        	test[read_test(adress+1, test)] = inp.pop()
	        else:
	        	test[relative_base + read_test(adress + 1, test)] = inp.pop()

	        if inf_loop:
	        	adress_map[machine] = adress + 2
	        	return -1, -1, -1
	        #print(relative_base, read_test(adress+1))
	        #print(first_param)
	        #print(read_test(1000))
	        #test[first_param] = input1

	    elif opcode == 4:
	        #print("value at address", adress + 1 , "is:", first_param)
	        #print("value:",first_param)
	        adr[machine] = adress + 2
	        if counter == 0:
	        	destination = first_param
	        elif counter == 1:
	        	x = first_param
	        elif counter == 2:
	        	y = first_param
	        	return destination, x, y

	        counter += 1
	        #return first_param

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
	                test[relative_base + read_test(adress + 3, test)] = 1
	            else:
	                test[relative_base  + read_test(adress +3, test)] = 0

	    elif opcode == 8:
	        #print(third_param)
	        if mode_third != 2:
	            if first_param == second_param:
	                test[third_param] = 1
	            else:
	                test[third_param] = 0
	        else:
	            if first_param == second_param:
	                test[relative_base + read_test(adress + 3, test)] = 1
	            else:
	                test[relative_base + read_test(adress + 3, test)] = 0

	    elif opcode == 9:
	        relative_base += first_param

	    if opcode < 3 or opcode > 6 and opcode < 9:
	        adress += 4

	    elif ((opcode == 5 or opcode == 6) and not jumped):
	        adress += 3

	    elif opcode == 3 or opcode == 4 or opcode == 9:
	        adress += 2
	    jumped = False

adress_map = dict()
input_buffer = dict()
for i in range(50):
	adress_map[i] = 0
	input_buffer[i] = []

for i in range(50):
	run_int_code([i], val, adress_map, i, input_buffer)
	
running = True
while running:
	for i in range(50):
		#print("running machine#",i)
		if not input_buffer[i]:
			packet = [-1]
		else:
			packet = input_buffer[i][0:2]
			
			input_buffer[i].pop()
			input_buffer[i].pop()
		
		#print("Packet is:", packet)
		dest, x, y = run_int_code(packet, val, adress_map, i, input_buffer)
		if dest != -1 and x != -1 and y != -1:
			input_buffer[dest] += [x,y]	
			print("*"*50)
			print(dest, x, y)
			running = False
			break
		if dest == 255:
			print(x,y)
			break
		

