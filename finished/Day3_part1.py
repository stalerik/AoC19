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

for e in first_wire:
    x2 = 0
    y2 = 0
    x1_temp = x1
    y1_temp = y1
    a,b = update_axis(e)
    x1 += a
    y1 += b
    wire_1_segments.append((int(x1_temp),int(y1_temp),int(x1),int(y1)))

for w in second_wire:
    x2_temp = x2
    y2_temp = y2
    c,d = update_axis(w)
    x2 += c
    y2 += d
    wire_2_segments.append((int(x2_temp), int(y2_temp), int(x2), int(y2)))


def between(start, end, point):
    return (start > point and end < point) or (start < point and end > point)

lengths = []

for e1 in wire_1_segments:
    for e2 in wire_2_segments:
        #checks if first wire is changing in y-axis and second wire is changing in x-axis.
        #Also controls that the x value of wire one is between the values wire two covers
        #The same is done for wire two's y value.
        if (e1[0] == e1[2] and between(e2[0], e2[2], e1[0])) and (e2[1] == e2[3] and between(e1[1],e1[3], e2[1])):
            lengths.append(e1[0]+e2[1])
        elif (e1[1] == e1[3] and between(e2[1], e2[3], e1[1])) and(e2[0] == e2[2] and between(e1[0], e1[2], e2[0])):
            lengths.append(e1[1]+e2[0])

print(min(lengths))

"""
        if check_intersections(x_diff1, x_diff2):
            x_intersections.append((x1, x2_temp, x2, y1, y2_temp, y2))
            print("X")
            print(e, "-------", w)
            print("x1: ", x1, " x2: ", x2, " x2bfr: ", x2_temp)
            print("y1: ", y1, " y2: ", y2, " y2bfr: ", y2_temp)
            print("-------------------------------------------")

        elif check_intersections(y_diff1, y_diff2):
            y_intersections.append((y1, y2_temp, y2))
            print("Y")
            print(e, "-------", w)
            print("x1: ", x1, " x2: ", x2, " x2bfr: ", x2_temp)
            print("y1: ", y1, " y2: ", y2, " y2bfr: ", y2_temp)
            print("-------------------------------------------")


print(x_intersections)
"""
