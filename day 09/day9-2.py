def readfile(filename):
	f = open(filename, "r")
	nums = []	
	for line in f:
		nums.append(int(line))
	f.close()
	return nums

nums = readfile("day9.txt")
test = 2089807806
for start in range(len(nums)-1):
	for end in range(start+2, len(nums)+1):
		trange = nums[start:end]
		if sum(trange) == test:
			print(min(trange) + max(trange))



