import os
import copy as cp

file = open(os.path.join(os.path.abspath(os.curdir), "input1000.txt"))
content = file.read()


old_input = []
for e in content:
	if e != '' and e != '\n':
		old_input.append(int(e))

print(len(old_input))

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
	

while True:
	

	new_input = []
	step = 0
	for j in range(len(old_input)):
		number = 0
		cur_pattern = update_pattern(step + 1)
		i = 1
		for k in range(len(old_input)):
			#print(k, i %len(old_input))
			number += old_input[k] * cur_pattern[i%len(cur_pattern)]
			i += 1
		step += 1

		new_input.append(abs(number)%10) 

	
	old_input = cp.copy(new_input)
	phase += 1
	line = ''
	print("Phase:", phase)
	
	if phase == 100:
		for e in new_input:
			line+=str(e)
		print(line)
		break