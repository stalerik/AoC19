import os


file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
wires = content.split("\n")

first_wire = wires[0].split(",")
second_wire = wires[1].split(",")

wire_map = []
"""
for i in range(10000):
    temp = []
    for i in range(10000):
        temp.append("")
    wire_map.append(temp)

print("wiremap done")

def update_map(instr, x, y):
    sign = ""
    steps = 0
    if(segment[0] == 'L'):
        sign = "-"
        steps = -(int(segment[1::]))

    elif(segment[0] == 'D'):
        sign = "|"
        stemps = -(int(segment[1::]))
    elif(segment[0] == 'R'):
        sign = "-"
        steps = (int(segment[1::]))
    elif(segment[0] == 'U'):
        sign = "|"
        steps = (int(segment[1::]))

x = 0
y = 0
for e in

"""
def update_axis(segment):
    upd_x = 0
    upd_y = 0
    if(segment[0] == 'L'):
        upd_x = -1
    elif(segment[0] == 'D'):
        upd_y = -1
    elif(segment[0] == 'R'):
        upd_x = 1
    elif(segment[0] == 'U'):
        upd_y = 1

    upd_x *= int(segment[1::])
    upd_y *= int(segment[1::])
    return(upd_x, upd_y)

def check_intersections(dist1, dist2):
    if (dist1 <= 0 and dist2 <= 0) or (dist1 >= 0 and dist2 >= 0):
        return False
    else:
        return True

wire_1_segments = []
wire_2_segments = []


x1 = 0
y1 = 0
first_steps = 0
for e in first_wire:
    x2 = 0
    y2 = 0
    x1_temp = x1
    y1_temp = y1
    a,b = update_axis(e)
    x1 += a
    y1 += b
    first_steps += abs(a + b)

    wire_1_segments.append((int(x1_temp),int(y1_temp),int(x1),int(y1), first_steps))

print("hello")
second_steps = 0
for w in second_wire:
    x2_temp = x2
    y2_temp = y2
    c,d = update_axis(w)
    x2 += c
    y2 += d
    second_steps += abs(c + d)

    wire_2_segments.append((int(x2_temp), int(y2_temp), int(x2), int(y2), second_steps))


def between(start, end, point):
    return (start > point and end < point) or (start < point and end > point)

lengths = []
steps = []
for e1 in wire_1_segments:
    for e2 in wire_2_segments:
        #checks if first wire is changing in y-axis and second wire is changing in x-axis.
        #Also controls that the x value of wire one is between the values wire two covers
        #The same is done for wire two's y value.

        #The value at index 5 is the total steps required to get to the end of the segment.
        #I then subtract the steps to the actual intersection. Not sure why i need to
        #use the "new" coordinate of the segment when doing this but that works.
        if (e1[0] == e1[2] and between(e2[0], e2[2], e1[0])) and (e2[1] == e2[3] and between(e1[1],e1[3], e2[1])):
            lengths.append(e1[0]+e2[1])
            steps.append((e1[4] - abs(e1[0] - e2[2])) + (e2[4] - abs(e1[3]-e2[1])))
            print(e1[4], "----", e2[4])

        elif (e1[1] == e1[3] and between(e2[1], e2[3], e1[1])) and(e2[0] == e2[2] and between(e1[0], e1[2], e2[0])):
            lengths.append(e1[1]+e2[0])
            steps.append((e1[4] - abs(e1[1] - e2[3])) + (e2[4] - abs(e1[2]-e2[0])))
            print(e1[4], "****", e2[4])

print(min(steps))
