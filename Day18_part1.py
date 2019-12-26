import os
import copy as cp

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
lines = content.split("\n")

board = dict()

for y, y_content in enumerate(lines):
	for x, x_content in enumerate(y_content):
		board[x,y] = x_content

print(board)