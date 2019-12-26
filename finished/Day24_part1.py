import os
import copy as cp
import time

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
lines = content.split("\n")

board = dict()
x= 0
y=0
for line in lines:
	for e in line:
		if e == '#':
			board[x,y] = 1
		else:
			board[x,y] = 0
		x += 1
	y += 1
	x= 0



def read_board(b, cords):
	if cords in b.keys():
		return b[cords]
	else:
		return 0

def cell_auto(b):
	board_copy = cp.copy(b)
	for y in range(5):
		for x in range(5):
			neighbours = 0
			neighbours += read_board(b,(x,y+1))
			neighbours += read_board(b,(x,y-1))
			neighbours += read_board(b,(x+1,y))
			neighbours += read_board(b,(x-1,y))
			#print(neighbours, x,y)
			if neighbours == 1 and read_board(b,(x,y)) == 1:
				board_copy[x,y] = 1
			elif (neighbours == 2 or neighbours == 1) and read_board(b, (x,y)) == 0:
				board_copy[x,y] = 1
			else:
				board_copy[x,y] = 0
	return board_copy

def calculate_answer(state):
	answer = 0
	for pwr, cell in enumerate(state):
		if cell == 1:
			#print(2**pwr)
			answer += 2**(pwr)
	return answer

saved_states = []
while True:
	total_line = []
	line = ""
	for y in range(5):
		for x in range(5):

			total_line.append(board[x,y])
			if board[x,y] == 1:
				line += '#'
			else:
				line += '.'
		print(line)
		line = ""

	if total_line in saved_states:
		
		print(calculate_answer(total_line))
		break

	saved_states.append(total_line)
	total_line = []
	board = cell_auto(board)
	print("\n\n\n")




