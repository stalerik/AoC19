import os
import copy as cp
import math

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
lines = content.split("\n")

height = len(lines)
width = len(lines[0])

asteroid_map = dict()
coordinates = []

for y, line in enumerate(lines):
	for x, asteroid in enumerate(line):
		if asteroid == '#':
			asteroid_map[(x,y)] = 1
		else:
			asteroid_map[(x,y)] = 0

		coordinates.append((x,y))


def slope(cord1, cord2):
	if cord1[1]-cord2[1] == 0:
		return 0
	elif cord1[0]-cord2[0] == 0:
		return 100000
	else:
		return (float(cord2[1]-cord1[1])/float(cord2[0]-cord1[0]))

def is_between(center, found, new):
	if found[0] == new[0]:
		if (new[1] > center[1] and found[1] > center[1]) or (new[1] < center[1] and found[1] < center[1]):
			return False
		elif (new[1] > center[1] and found[1] < center[1]) or (new[1] < center[1] and found[1] > center[1]):
			return True 
			#vilken ska bli True och vilken False. Problemet ligger här!

	if (new[0] > center[0] and found[0] > center[0]) or (new[0] < center[0] and found[0] < center[0]):
		return False
	else:
		return True

results = []
saved_slopes = dict()

base = (23,19)
for c in coordinates:
	saved_slopes.clear()
	count = 0
	saved_cords = []

	if asteroid_map[c] == 1:
		for e in coordinates:
			if e != c and asteroid_map[e] == 1:
				s = slope(c,e)
				if s in saved_slopes.keys():
					flag = True
					temp = cp.copy(saved_slopes[s])

					for cord in temp:
						#print(c, e, temp, is_between(c,e,cord), s)
						if not is_between(c,e,cord):
							flag = False


					if flag:
						saved_cords.append(e)
						count += 1
					saved_slopes[s].append(e)

				else:
					saved_slopes[s] = [e]
					saved_cords.append(e)
					count += 1

		results.append((c, count, saved_cords, cp.copy(saved_slopes)))



biggest = 0
for e in results:
	if e[1] > biggest:
		biggest = e[1]
		saved = e

print(saved[3][2.142857142857143])

temp = saved[2]

#Kan se över 200 asteroied, så jag kommer inte behöva köra ett helt varv.
#Måste sortera dem på något vis.

def angle_between(cord):
	distance = math.sqrt((base[0] - cord[0])**2 + (base[1] - cord[1])**2)
	multiplier = 0
	rads = 0
	x = cord[0] - base[0]
	y = base[1] - cord[1]
	print(x,y)
	if x > 0 and y < 0 or x < 0 and y < 0:
		multiplier = math.pi
		#print("hey")
	if x < 0 and y > 0:
		multiplier = 2*math.pi
		print("uoo")
		rads =  (-math.atan(y/x) - math.pi/2) + multiplier
		return math.degrees(rads)

	if x > 0 and y > 0:
		rads = math.pi/2 - math.pi + math.atan(y/x)
		return math.degrees(rads)

	
	if x == 0:
		if cord[1] < base[1]: #Över basen
			return math.degrees(0)
		else:
			return math.degrees((math.pi))
	if y == 0:
		if cord[0] > base[0]:
			return math.degrees(math.pi/2)
		else:
			return math.degrees(3*math.pi/2)
	else:
		rads = math.atan(y/x) 	
	return math.degrees(rads+multiplier)

#print(base)
#print(math.degrees((math.pi+ math.pi/2)))
#print(angle_between((22,19)))
sorted_ast = sorted(temp, key=angle_between, reverse=False)

#for e in sorted_ast:
#	print(e, angle_between(e))

print(sorted_ast[199])






