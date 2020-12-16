import re

def readmask(value):
	mask = 0
	covers = [0]
	for char in value:
		if char == "X":
			mask *= 2
			covers = [(x*2)+k for x in covers for k in range(2)]
		elif char == "1":
			mask *= 2
			covers = [(x*2)+1 for x in covers]
		elif char == "0":
			mask = (mask*2)+1
			covers = [x*2 for x in covers]
	return (mask, covers)

def putval(action, value, mem, mask, covers):
	pos = int(re.search('\[(.*)\]', action).group(1))
	val = int(value)
	for cover in covers:
		mem[(pos & mask) | cover] = val


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