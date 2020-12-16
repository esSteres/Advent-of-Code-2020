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

def move(x, y, dir, dist):
	if dir == "N":
		return (x, y+dist)
	if dir == "E":
		return (x+dist, y)
	if dir == "S":
		return (x, y-dist)
	if dir == "W":
		return (x-dist, y)

steps = readfile("day12.txt")

dirmap = { 0 : "E", 1 : "S", 2 : "W", 3 : "N" }
facing = 0
x = 0
y = 0

for (action, num) in steps:
	if action == "L":
		facing = (facing - num) % 4
	elif action == "R":
		facing = (facing + num) % 4
	elif action == "F":
		(x, y) = move(x, y, dirmap[facing], num)
	else:
		(x, y) = move(x, y, action, num)

print("X:", x, "Y:", y, "mdist:", abs(x) + abs(y))