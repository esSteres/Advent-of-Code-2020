input = [7,14,0,17,11,1,2]
ages = {}
for i in range(len(input)-1):
	ages[input[i]] = i+1

currn = input[-1]
time = len(input)
while time < 30000000:
	nextn = 0
	if currn in ages:
		nextn = time - ages[currn]
	ages[currn] = time
	currn = nextn
	time += 1

print (currn)