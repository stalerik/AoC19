import os
import copy as cp

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
	print("HOW??")

results = []
saved_slopes = dict()
for c in coordinates:
	saved_slopes.clear()
	count = 0
	saved_cords = []

	if asteroid_map[c] == 1:
		#print("coordinate:", c)
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

		results.append((c, count))


biggest = 0
for e in results:
	if e[1] > biggest:
		biggest = e[1]
		saved = e
print(biggest, saved)





