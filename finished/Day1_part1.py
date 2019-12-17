import os

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
lines = content.split("\n")

def mass_calculator(mass):
	return (int(mass/3)-2)

total_fuel = 0

for line in lines:
	print(line)
	print(mass_calculator(int(line)))
	total_fuel += mass_calculator(int(line))
print(total_fuel)

