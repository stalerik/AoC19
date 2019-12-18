import os
import copy as cp
import math

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
moon_inp = content.split("\n")

#Update the velocity with gravity, then update the pos with velocity
moon_pos = dict()
moon_vel = dict()
for i, m in enumerate(moon_inp):
	if m == "":
		break
	m = m.replace('<','')
	m = m.replace('>','')
	x, y, z = m.split(",")
	moon_pos[i] = [int(x[2:]), int(y[3:]), int(z[3:])]
	moon_vel[i] = [0,0,0]

def update_vel(axis):
	for i in range(4):
		first_pos = moon_pos[i]
		first_vel = moon_vel[i]
		for j in range(i+1,4):
			second_pos = moon_pos[j]
			second_vel = moon_vel[j]
			
			if first_pos[axis] < second_pos[axis]:
				first_vel[axis] += 1
				second_vel[axis] -= 1
					

			elif first_pos[axis] > second_pos[axis]:
				first_vel[axis] -= 1
				second_vel[axis] += 1

			moon_vel[i] = first_vel
			moon_vel[j] = second_vel


def update_pos(axis):
	for i in range(4):
		pos = moon_pos[i]
		vel = moon_vel[i]
		
		
		pos[axis] += vel[axis]

		moon_pos[i] = pos

def inc_axis(axis):
	if axis == 2:
		return 0
	else:
		return axis + 1

i = 0
"""
saved = dict()
saved[0] = []
saved[1] = []
saved[2] = []

times = dict()
times[0] = []
times[1] = []
times[2] = []
"""
start_pos = ([16, -8, 13], [4, 10, 10], [17, -5, 6], [13, -3, 0])
#start_pos = ([-8,-10, 0],[5,5,10],[2,-7,3],[9,-8,-3] )
compare = [x[0] for x in start_pos]

axis = 0
while True:
	update_vel(axis)
	update_pos(axis)
	
	all_pos = []
	velocity = []
	for j in range(4):
		all_pos.append(moon_pos[j][axis])
		velocity.append(moon_vel[j][axis])
		
	i += 1
	if all_pos == compare and velocity == [0,0,0,0]:
		print(axis, i)
		axis = inc_axis(axis)
		compare = [x[axis] for x in start_pos]
		i = 0
		if axis == 0:
			#TODO
			#Calculate the LCM here and print
			break
		
	
	

	"""
	if all_pos in saved[axis]:
		if i not in times:
			times[axis].append(i)
			print("x-cycles:",times[0])
			print("y-cycles:",times[1])
			print("z-cycles:",times[2])
			print("----------------")
			steps[axis] = i
			axis = inc_axis(axis)
			i = steps[axis]
			lastx = 0
			lasty = 0
			lastz = 0
			for x in range(len(times[0])):

				for y in range(len(times[1])):
					for z in range(len(times[2])):
						#if x == y and x == z and y == z:
							print(x - lastx, y- lasty, z-lastz)
							print("Right answer")
							print(x,y,z)

						#print(x,y,z)	
			#print("****************")
	else:
		saved[axis].append(all_pos)
	"""


