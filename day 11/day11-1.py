import copy

def readfile(filename):
	f = open(filename, "r")
	out = []
	for line in f:
		out.append([char for char in line[:-1]])
	f.close()
	return out

def countadj(row, col, grid):
	total = 0
	for r in range(max(0, row-1), min(len(grid), row+2)):
		for c in range(max(0, col-1), min(len(grid[r]), col+2)):
			if grid[r][c] == "#" and not (r == row and c == col):
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
			elif grid[r][c] == "#" and n >= 4:
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
