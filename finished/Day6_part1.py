import os

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
lines = content.split("\n")

orbits = content.split(")")


o_map = dict()
parents = set()
children = set()

for line in lines:
    if line == "":
        break;

    temp = line.split(")")
    parent = temp[0]
    child = temp[1]
    parents.add(parent)
    children.add(child)
    flag = False
    if parent in o_map.keys():
        o_map[parent].append(child)
    else:
        o_map[parent] = [child]


#find the root
for p in parents:
    if p not in children:
        root = p

print(root)

#Calculate orbits
def r_orbs(current, cost):
    if current not in o_map.keys():
        return cost
    else:
        temp_cost = 0
        for c in o_map[current]:
            temp_cost += r_orbs(c, cost+1)

        return cost + temp_cost


print(r_orbs(root, 0))
