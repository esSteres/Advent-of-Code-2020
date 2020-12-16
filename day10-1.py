def readfile(filename):
	f = open(filename, "r")
	nums = []
	for line in f:
		nums.append(int(line))
	f.close()
	return nums

nums = readfile("day10.txt")
nums.sort()
diffs = {x : 0 for x in range(4)}
last = 0
for val in nums:
	diffs[val-last] += 1
	last = val
diffs[3] += 1
print(diffs)
print(diffs[1] * diffs[3])