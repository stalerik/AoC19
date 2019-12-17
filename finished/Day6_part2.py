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

    if child in o_map.keys():
        o_map[child].append(parent)
    else:
        o_map[child] = [parent]



start = 'YOU'
end = 'SAN'
print(end in parents)


def r_find(current, prev, visited):
    if current == end:
        print("Eureka")
    else:
        #print(visited)
        for c in o_map[current]:
            if c not in visited:
                prev[c] = current
                r_find(c, prev, visited+[current])

p = dict()
r_find(start, p, [])

c = end
tot = 0
while c != start:
    c = p[c]
    tot += 1
print(tot)
