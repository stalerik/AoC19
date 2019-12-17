import os
from collections import deque

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
lines = content.split("\n")

req_map = dict()

for line in lines:
	reqs, goal = line .split("=>")
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
			req_map[key].append((r_amount,r_resource))

	else:
		r_amount, r_resource = reqs.split()
		r_amount = int(r_amount)
		req_map[key].append((r_amount,r_resource))

start = (1, 'FUEL')
material_map = {}


for e in req_map.keys():
	material_map[e[1]] = 0


def find_fuel(start):
	q = deque()
	q.append(start)
	total = 0
	while q:
		goal = q.pop()
		needed = goal[0]
		print(material_map['A'])
		for e in req_map.keys():
			if e[1] == goal[1]:
				increment = e[0]
				mat = e[1]
				key = e

		for e in req_map[key]:
			if e[1] == 'ORE':
				total += needed
			else:
				material_map[e[1]] += needed * e[0]
		
		for e in req_map[key]:
			if e[1] != 'ORE':
				q.append((material_map[e[1]], e[1]))
	print(total)
	print(material_map)

	return total

find_fuel(start)
