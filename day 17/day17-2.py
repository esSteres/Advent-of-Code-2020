activepts = set()

f = open("day17.txt", "r")
y = 0
for line in f:
	for x in range(len(line)-1):
		if line[x] == "#":
			activepts.add((x, y, 0, 0))
	y += 1

def getadjacent(point):
	return ((x,y,z,w) 
		for x in range(point[0]-1, point[0]+2) 
		for y in range(point[1]-1, point[1]+2) 
		for z in range(point[2]-1, point[2]+2) 
		for w in range(point[3]-1, point[3]+2) 
		if not (x,y,z,w) == point)

def isactivenext(point, activepts):
	activeadj = 0
	for adj in getadjacent(point):
		if adj in activepts:
			activeadj += 1
	if point in activepts:
		if activeadj in range(2, 4):
			return True
		else:
			return False
	else:
		if activeadj == 3:
			return True
		else: 
			return False

def step(activepts):
	newactive = set()
	testedpts = set()
	for point in activepts:
		if isactivenext(point, activepts):
			newactive.add(point)

		for adj in getadjacent(point):
			if adj in activepts or adj in testedpts:
				continue

			if isactivenext(adj, activepts):
				newactive.add(adj)

			testedpts.add(adj)

	return newactive

for i in range(6):
	activepts = step(activepts)

print(len(activepts))


