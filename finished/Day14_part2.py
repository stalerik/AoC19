import os
from queue import *
import math

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
lines = content.split("\n")

req_map = dict()

for line in lines:
	reqs, goal = line.split("=>")
	g_amount, g_resource = goal.split()
	g_amount = int(g_amount)
	key = (g_amount, g_resource)
	if key not in req_map.keys():
		req_map[key] = []

	if "," in reqs:
		reqs = reqs.split(",")
		for req in reqs:
			r_amount, r_resource = req.split()
			r_amount = int(r_amount)
			req_map[key].append([r_amount,r_resource])

	else:
		r_amount, r_resource = reqs.split()
		r_amount = int(r_amount)
		req_map[key].append([r_amount,r_resource])

start = 'FUEL'
needed_amount = {}


for e in req_map.keys():
	needed_amount[e[1]] = 0


def find_fuel(start, amount):
	needed_amount['FUEL'] = amount
	q = Queue()
	q.put(start)
	total = 0
	while not q.empty():

		goal = q.get()
		
		#print("current instruction:", goal)
		
		for e in req_map.keys():
			if e[1] == goal:
				increment = e[0]
				mat = e[1]
				key = e
		flag = False
		for e in req_map[key]:
			if e[1] == 'ORE':
				amount = math.ceil(needed_amount[mat]/increment)
				needed_amount[mat] -= amount*increment
				total += e[0]*amount
				#while needed_amount[mat] > 0:
				#	total += e[0]
				#	needed_amount[mat] -= increment
			else:
				flag = True #The flag is needed so we use the same value for all required mats
				temp = needed_amount[mat]
				amount = math.ceil(needed_amount[mat]/increment)
				needed_amount[e[1]] += e[0]*amount

				#while temp > 0:
				#	needed_amount[e[1]] += e[0]
				#	temp -= increment
		if flag:
			needed_amount[mat] -= amount*increment
		
		for e in req_map[key]:
			if e[1] != 'ORE':
				q.put(e[1])

		#print(needed_amount)
	#print(total)
		
		

	return total

#print(find_fuel('FUEL',1))


#Trying a binary search for this. Know the answer is between 2^17 and 2^18
req_ore = 0
max_ore = 1000000000000
fuel = 1
lower_bound = 1
upper_bound = 0
while lower_bound +1 != upper_bound:
	if upper_bound == 0:
		fuel = lower_bound*2
	else:
		fuel = (lower_bound + upper_bound)//2

	req_ore = find_fuel('FUEL',fuel)
	print(req_ore, fuel)
	print(lower_bound, upper_bound)
	print("\n")

	
	if req_ore < max_ore:
		lower_bound = fuel
	else:
		upper_bound = fuel

print("Answer is:", lower_bound+1)
	
	

