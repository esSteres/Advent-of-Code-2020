def readfile(filename):
	f = open(filename, "r")
	nums = []
	for line in f:
		nums.append(int(line))
	f.close()
	return nums

def countperms(start, rest, memo):
	if start in memo:
		return memo[start]
	if rest == []:
		return 1
	total = 0
	for i in range(3):
		if i < len(rest) and rest[i]-start <= 3:
			total += countperms(rest[i], rest[i+1:], memo)
	memo[start] = total
	return total

nums = readfile("day10.txt")
nums.sort()
print(nums)
print(countperms(0, nums, {}))