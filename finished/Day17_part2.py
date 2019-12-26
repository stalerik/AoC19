import os
import copy as cp
import time
from queue import *

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
values = content.split(",")

val = dict()
for i in range(len(values)):
    val[i] = int(values[i])

#From challange
val[0] = 2

current_instruction = 0
adress = 0
relative_base = 0

jumped = False

def read_test(addr, test):
    if addr in test.keys():
        return(test[addr])
    else:
        return 0


def run_int_code(inp, test, adr):
	adress = adr[0]
	global relative_base
	line = ""
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
	    #print("adress:", adress, "opcode:", opcode)

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
	        
	        
	        print(inp)
	        if not inp:
	        	return
	        if mode_first != 2:
	            test[read_test(adress+1, test)] = inp.pop(0)
	        else:
	            test[relative_base + read_test(adress + 1, test)] = inp.pop(0)
	        #print(relative_base, read_test(adress+1))
	        #print(first_param)
	        #print(read_test(1000))
	        #test[first_param] = input1

	    elif opcode == 4:
	        #print("value at address", adress + 1 , "is:", first_param)
	        #print("value:",first_param)
	        #adr[0] = adress + 2
	        if first_param == 10:
	        	print(line)
	        	line = ""
	        	#time.sleep(0.05)
	        elif first_param > 255:
	        	print(first_param)
	        else:
	        	line += chr(first_param)
	        
	        #if first_param > 255:
	        #	print(first_param)

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

adress_map = {0:0}
line = ""
board = dict()
x = 0
y = 0
#main program
main_prog = 'A,B,A,C,A,B,C,A,B,C\n'

#A
A = 'R,12,R,4,R,10,R,12\n'
#B
B = 'R,6,L,8,R,10\n'
#C
C ='L,8,R,4,R,4,R,6\n'

no = 'n\n'

# 35 == #

print("main_prog")
print("*"*50)
inp = []
for e in main_prog:
	inp.append(ord(e))
#print(inp)
#run_int_code(inp, val, adress_map)
#inp = []


for e in A:
	inp.append(ord(e))

#run_int_code(inp, val, adress_map)
#inp = []
for e in B:
	inp.append(ord(e))

#run_int_code(inp, val, adress_map)
#inp = []
for e in C:
	inp.append(ord(e))
#run_int_code(inp, val, adress_map)
#inp = []
for e in no:
	inp.append(ord(e))

res = run_int_code(inp, val, adress_map)

print(res)
while True:
	res = run_int_code(1, val, adress_map)
	print(res)
	
#path
#R12,R4,R10,R12,R6,L8,R10,R12,R4,R10,R12,L8,R4,R4,R6,R12,R4,R10,R12,R6,L8,R10,L8,R4,R4,R6,R12,R4,R10,R12,R6,L8,R10,L8,R4,R4,R6


