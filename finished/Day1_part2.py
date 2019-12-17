import os

file = open(os.path.join(os.path.abspath(os.curdir), "input.txt"))
content = file.read()
lines = content.split("\n")

def mass_calculator(mass):
	return (int(mass/3)-2)

total_fuel = 0
for line in lines:
	mass_fuel = mass_calculator(int(line))
	total_fuel += mass_fuel
	req_fuel = mass_calculator(mass_fuel)
	while req_fuel > 0:
		total_fuel += req_fuel
		req_fuel = mass_calculator(req_fuel)

print(total_fuel)



