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



board = {}
tile_id = 0
cords = (0,0)
adress_map = {0:0}
count = 0
user_inp = 0
x = 0
y = 0
count = 0
first = True
score = 0

low_y = 100
low_x = 100
high_y = -100
high_x = -100
def init_paint():
	global low_y,low_x,high_x,high_y
	plane = board.keys()
	for e in plane:
		if e[1] < low_y:
			low_y = e[1]
		if e[0] < low_x:
			low_x = e[0]
		if e[1] > high_y:
			high_y = e[1]
		if e[0] > high_x:
			high_x = e[0]




#print(low_x, high_x)
#print(low_y, high_y)

def paint_board():
	global score

	print("\n\n\n\n\n\n")
	for y in range(high_y, low_y - 1, -1):
		line = ""
		for x in range(low_x, high_x+1):
			if (x,y) in board.keys():
				char = board[x,y]
			else:
				char = 0
			if x == -1 and y == 0:
				score = char
			if char == 0:
				line += ' '
			elif char == 1:
				line += '#'
			elif char == 2:
				line += '*'
			elif char == 3:
				line += '-'
				player_x = x
			elif char == 4:
				line += 'o'
				ball_x = x

		print(line)
	print("SCORE:",score)
	return player_x, ball_x



def read_test(addr, test):
    if addr in test.keys():
        return(test[addr])
    else:
        return 0


def run_int_code(inp, test, adr):
	adress = adr[0]
	global relative_base, first
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
	        paint_board()
	        print("Halted")
	        return -101

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
	        
	        #special case. always imidiate mode here
	        time.sleep(0.016)
	        if first:
	        	init_paint()
	        	first = False
	        p_x, b_x = paint_board()
	        if p_x < b_x:
	        	inp = 1
	        elif p_x > b_x:
	        	inp = -1
	        else:
	        	inp = 0
	        	"""
	        while True:
		        u_inp = input("opcode is 3: ")
		        if u_inp =='d':
		        	inp = 1
		        	break
		        elif u_inp == 'a':
		        	inp = -1
		        	break
		        elif u_inp == '':
		        	inp = 0
		        	break
		       	else:
		       		print("New input pls")
				"""
	        paint_board()
	        if mode_first != 2:
	            test[read_test(adress+1, test)] = inp
	        else:
	            test[relative_base + read_test(adress + 1, test)] = inp
	        #print(relative_base, read_test(adress+1))
	        #print(first_param)
	        #print(read_test(1000))
	        #test[first_param] = input1

	    elif opcode == 4:
	        #print("value at address", adress + 1 , "is:", first_param)
	        #print("value:",first_param)
	        adr[0] = adress + 2
	        return first_param

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

def new_direction(current, output):
	if output == 0: #Left
		if current == (0,1):
			return (-1,0)
		elif current == (-1,0):
			return (0,-1)
		elif current == (0,-1):
			return (1,0)
		elif current == (1,0):
			return (0,1)

	elif output == 1: #Right
		if current == (0,1):
			return (1,0)
		elif current == (1,0):
			return (0,-1)
		elif current == (0,-1):
			return (-1,0)
		elif current == (-1,0):
			return (0,1)
	else:
		print(output)
		return -1







while True:
	#user_input = int(input("-1 left 1 right"))
	x = run_int_code(user_inp, val, adress_map)
	if x == -101:
		break

	y = run_int_code(user_inp, val, adress_map) 
	if y == -101:
		break
	tile_id = run_int_code(user_inp, val, adress_map)
	if tile_id == -101:
		print("tile")
		break
	if tile_id == 2:
		count += 1
	board[(x,y)] = tile_id





