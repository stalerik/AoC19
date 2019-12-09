import os

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()

zeroes = 0
ones = 0
twos = 0

layer_map = dict()
layer = []
layers = 0

last = 0
for i in range(len(content)):
    if i % 25 == 0 and i != 0:
        line = content[last:i]
        #print(line)
        layer.append(line)

        last = i
        #h += 1
        if i % 150 == 0 and i:
            l = i/150
            layer_map[l] = layer
            layer = []
            layers += 1

image_map = dict()
#populate the image
for i in range(151):
    image_map[i] = '2'

#print(layer_map[1])
#The image is the first layer
current_layer = layer_map[1]
for i in range(layers):
    current_layer = (layer_map[i+1])
    for line_number, line_content in enumerate(current_layer):
        for pixel_number, pixel_content in enumerate(line_content):

            if image_map[(line_number*25) + pixel_number] == '2':
                image_map[line_number*25 + pixel_number] = pixel_content

l = ""

for i in range(151,0, -1):
    image_map[i] = image_map[i-1]

for i in range(151):
    l+=image_map[i]
    if i % 25 == 0:
        print(l)
        l = ""
