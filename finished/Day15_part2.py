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


board = {(0,0):0}

def paint_board(droid, board):
	#print("\n\n\n\n\n\n") #"Clear" the board
	print("*"*50)
	for y in range(25, -26, -1):
		line = ""
		for x in range(-28, 32):
			#if (x,y) == droid:
			#	char = 2
			if (x,y) in board.keys():
				char = board[x,y]
			else:
				char = 0

			if char == 0: #Undiscovered
				line += ' '
			elif char == 1: #Wall
				
				line += '#'
			elif char == 2: #Droid
				line += '*'
			elif char == 3: #Discovered
				line += '.'
			elif char == 4: #Oxygen-place
				line += 'x'
			else:
				line += 'O'
				#print(x,y) -12,12

		print(line)
	print("*"*50)
	

def update_direction(direction, res):
	if res == 1:
		if direction == 1:
			return 3
		elif direction == 3:
			return 2
		elif direction == 2:
			return 4
		else:
			return 1
	else:
		if direction == 1:
			return 4
		elif direction == 4:
			return 2
		elif direction == 2:
			return 3
		else:
			return 1

#1 NORTH
#2 SOUTH
#3 WEST
#4 EAST
cords = (0,0)
direction = 1
counter = 0
while True:
	counter += 1
	#direction = int(input("Enter direction: "))
	result = run_int_code(direction, val, {0:0})
	
	if result == -101:
		print("Halted")
		break


	saved_cords = cp.copy(cords)
	if direction == 1:
 		cords = (cords[0], cords[1]+1)
	elif direction == 2:

 		cords =(cords[0], cords[1]-1)
 		
	elif direction == 3:
 		cords = (cords[0]-1, cords[1])
	elif direction == 4:
 		cords = (cords[0]+1, cords[1])

	#print(saved_cords)
	if result == 0: #wall
 		board[cords] = 1
 		cords = saved_cords
	elif result == 1:
 		board[cords] = 3
	else:
 		board[cords] = 4

	direction = update_direction(direction,result)
	if cords == (0,0) and counter > 100:
		break

print(board[-12,12])
neighbours = dict()
def create_neighbours(board):

	for y in range(25, -26, -1):
		for x in range(-30, 36):
			if (x,y) in board.keys():
				if board[x,y] == 3 or board[x,y] == 4:
					for i in [-1,1]:
						if (x+i,y) in board.keys():
							if (board[x+i,y] == 3 or board[x+i,y] == 4):
								if (x,y) in neighbours.keys():
									neighbours[x,y].append((x+i,y))
								else:
									neighbours[x,y] = [(x+i, y)]


						if (x,y+i) in board.keys():
							if (board[x,y+i] == 3 or board[x,y+i] == 4):
								if (x,y) in neighbours.keys():
									neighbours[x,y].append((x,y+i))
								else:
									neighbours[x,y] = [(x, y+i)]

create_neighbours(board)

cost_map = {(-12,12):0}
paint_board(cords, board)
#start at 0,0 end at 12,-12
previous = {(0,0):-1}
def find_route(start, end):
	visited = set()
	q = Queue()
	q.put(start)
	current = start
	running = True
	cost = 0
	
	while not q.empty():
		current = q.get()
		if current not in visited:
			
			
			board[current] = 5
			visited.add(current)
			#print(current)
			paint_board(current, board)
			print("Minutes:", cost_map[current])
			time.sleep(0.04)
			for e in neighbours[current]:
				if e in cost_map.keys():
					cost = cost_map[e]
				else:
					cost = 99999999

				if e not in visited and cost > cost_map[current] + 1:

					cost_map[e] = cost_map[current] + 1
					q.put(e)
					#visited.add(e)
					previous[e] = current
					if e == end:
						#print("poopo")
						running = False

find_route((-12,12), (0,0))


#print(cost_map[-12,12])

