import os
import copy as cp

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()


old_input = []
for e in content:
	if e != '' and e != '\n':
		old_input.append(int(e))



base_pattern = [0, 1, 0, -1]

new_pattern = []
step = 0
phase = 0
first = True

def update_pattern(n):
	global base_pattern
	pattern = []
	for e in base_pattern:
		for i in range(n):
			pattern.append(e)

	return pattern

offset = 5975803	
old_input = old_input*10000
new_input = cp.copy(old_input)

while True:
	current_sum = 0
	for j in range(len(old_input)-1, offset-1, -1):
		current_sum += old_input[j]
		
		new_input[j] = current_sum%10

	
	old_input = cp.copy(new_input)
	phase += 1
	line = ''
	print("Phase:", phase)
	
	if phase == 100:
		for e in new_input[offset:offset+8]:
			line += str(e)
		print(line)
		break