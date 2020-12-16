def search(path, low, high):
	if len(path) == 1:
		return low if path == "F" or path == "L" else high-1
	elif path[0] == "F" or path[0] == "L":
		return search(path[1:], low, high-((high-low)/2))
	else:
		return search(path[1:], low+((high-low)/2), high)

def decode(bpass):
	row = search(bpass[:7], 0, 128)
	col = search(bpass[-3:], 0, 8)
	return (row*8) + col

f = open("day5.txt", "r")
seats = [False for i in range(865)]
for line in f:
	currid = decode(line[:-1])
	seats[int(currid)] = True

for i in range(1, 864):
	if  (not seats[i]) and seats[i-1] and seats[i+1]:
		print(i)
		break