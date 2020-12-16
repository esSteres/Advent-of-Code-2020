def readfile(filename):
	f = open(filename, "r")
	steps = []
	for line in f:
		action = line[:1]
		num = int(line[1:-1])
		if action == "R" or action == "L":
			num = num/90
		steps.append((action, num))
	f.close()
	return steps

steps = readfile("day12.txt")

actions = {
	"N" : lambda wx, wy, x, y, val : (wx, wy + val, x, y),
	"S" : lambda wx, wy, x, y, val : (wx, wy - val, x, y),
	"E" : lambda wx, wy, x, y, val : (wx + val, wy, x, y),
	"W" : lambda wx, wy, x, y, val : (wx - val, wy, x, y),
	"L" : lambda wx, wy, x, y, val : (wx*pow(1j, val).real - wy*pow(1j, val).imag, wx*pow(1j, val).imag + wy*pow(1j, val).real, x, y),
	"R" : lambda wx, wy, x, y, val : (wy*pow(1j, val).imag + wx*pow(1j, val).real, wy*pow(1j, val).real - wx*pow(1j, val).imag, x, y),
	"F" : lambda wx, wy, x, y, val : (wx, wy, x+(wx*val), y+(wy*val)),
}

wx = 10
wy = 1
x = 0
y = 0

for (action, num) in steps:
	(wx, wy, x, y) = actions[action](wx, wy, x, y, num)

print("X:", x, "Y:", y, "mdist:", abs(x) + abs(y))