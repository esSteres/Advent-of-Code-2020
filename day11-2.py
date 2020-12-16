import copy

def readfile(filename):
	f = open(filename, "r")
	out = []
	for line in f:
		out.append([char for char in line[:-1]])
	f.close()
	return out

def canseeoccupied(row, col, dr, dc, grid):
	r = row + dr
	c = col + dc
	while r in range(len(grid)) and c in range(len(grid[r])) and grid[r][c] == ".":
		r += dr
		c += dc
	if r in range(len(grid)) and c in range(len(grid[r])) and grid[r][c] == "#":
		return True
	return False

def countadj(row, col, grid):
	total = 0
	for dr in range(-1, 2):
		for dc in range(-1, 2):
			if not (dr == 0 and dc == 0) and canseeoccupied(row, col, dr, dc, grid):	
				total += 1

	return total

def step(grid):
	changes = 0
	ngrid = copy.deepcopy(grid)
	for r in range(len(grid)):
		for c in range(len(grid[r])):
			if grid[r][c] == ".":
				continue

			n = countadj(r, c, grid)
			if grid[r][c] == "L" and n == 0:
				ngrid[r][c] = "#"
				changes += 1
			elif grid[r][c] == "#" and n >= 5:
				ngrid[r][c] = "L"
				changes += 1

	return (ngrid, changes)

def formatgrid(grid):
	return "\n".join(["".join(row) for row in grid]) + "\n"

grid = readfile("day11.txt")
changes	= -1
while not changes == 0:
	(grid, changes) = step(grid)

filled = 0
for row in grid:
	for seat in row:
		if seat == "#":
			filled += 1
print(filled)
