def readfile(filename):
	f = open(filename, "r")
	nums = []	
	for line in f:
		nums.append(int(line))
	f.close()
	return nums

def checksum(array, sum):
	for n1 in range(len(array)):
		for n2 in range(len(array)):
			if (not n1 == n2) and (array[n1] + array[n2] == sum):
				return True
	return False

nums = readfile("day9.txt")
preamble = 25
for i in range(len(nums)):
	if i < preamble:
		continue
	if not checksum(nums[i-preamble:i], nums[i]):
		print(nums[i])



