import os
from queue import *

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
				while needed_amount[mat] > 0:
					total += e[0]
					
					needed_amount[mat] -= increment
			else:
				flag = True
				temp = needed_amount[mat]
				while temp > 0:
					needed_amount[e[1]] += e[0]
					temp -= increment
		if flag:
			needed_amount[mat] = temp
		
		for e in req_map[key]:
			if e[1] != 'ORE':

				q.put(e[1])

		#print(needed_amount)
	#print(total)
		
		

	return total

print(find_fuel(start,1))
