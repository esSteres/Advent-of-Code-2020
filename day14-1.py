import re

def readmask(value):
	mask = 0
	cover = 0
	for char in value:
		if char == "X":
			mask = (mask*2)+1
			cover *= 2
		else:
			mask *= 2
			cover = (cover*2) + int(char)
	return (mask, cover)

def putval(action, value, mem, mask, cover):
	pos = int(re.search('\[(.*)\]', action).group(1))
	mem[pos] = (int(value) & mask) | cover


mask = 0
cover = 0
mem = {}
f = open("day14.txt", "r")
for line in f:
	(action, p, value) = line[:-1].partition(" = ")
	if action == "mask":
		(mask, cover) = readmask(value)
	else:
		putval(action, value, mem, mask, cover)

f.close()

total = 0
for key in mem:
	total += mem[key]
print(total)