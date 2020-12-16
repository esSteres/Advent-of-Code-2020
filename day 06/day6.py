f = open("day6.txt", "r")

def countans(answers, gcount):
	total = 0
	for ans in answers:
		if answers[ans] == gcount:
			total += 1
		answers[ans] = 0
	return total

total = 0
answers = dict.fromkeys("a b c d e f g h i j k l m n o p q r s t u v w x y z".split(), 0)
gcount = 0
for line in f:
	if line == "\n":
		total += countans(answers, gcount)
		gcount = 0
	else:
		gcount += 1
		for char in line:
			if char != '\n':
				answers[char] += 1
total += countans(answers, gcount)
print(total)