def readfile(filename, code):
	f = open(filename, "r")
	for line in f:
		(inst, sp, num) = line[:-1].partition(" ")
		code.append((inst, int(num)))
	f.close()

decode = {
	"acc" : lambda step, acc, val: (step + 1, acc + val),
	"jmp" : lambda step, acc, val: (step + val, acc),
	"nop" : lambda step, acc, val: (step + 1, acc)
}

def exec(step, acc, canswap, code, visited):
	if step >= len(code):
		return acc
	if step in visited:
		return None
	visited.add(step)

	(inst, val) = code[step]
	(nstep, nacc) = decode[inst](step, acc, val)
	rest = exec(nstep, nacc, canswap, code, visited)
	
	if rest == None and canswap and not inst == "acc":
		if inst == "nop":
			inst = "jmp"
		else:
			inst = "nop"
		(nstep, nacc) = decode[inst](step, acc, val)
		return exec(nstep, nacc, False, code, visited)
	else:
		return rest

code = []
readfile("day8.txt", code)
print(exec(0, 0, True, code, set()))