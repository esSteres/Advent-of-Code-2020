def readfile(filename, code):
	f = open(filename, "r")
	for line in f:
		(inst, sp, num) = line[:-1].partition(" ")
		code.append((inst, int(num)))
	f.close()

code = []
step = 0
acc = 0
visited = set()

decode = {
	"acc" : lambda val: (step+1, acc + val),
	"jmp" : lambda val: (step+val, acc),
	"nop" : lambda val: (step+1, acc)
}

readfile("day8.txt", code)

while not step in visited:
	visited.add(step)
	(inst, val) = code[step]
	(step, acc) = decode[inst](val)

print(acc)

