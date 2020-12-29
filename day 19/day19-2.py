rules = {}
messages = []

f = open("day19.txt", "r")
line = f.readline()
while not line == "\n":
	(num, p, rule) = line.partition(": ")
	if '"' in rule:
		rules[int(num)] = rule[1]
	else:
		rules[int(num)] = [ [int(x) for x in option.split(" ")] for option in rule.split(" | ") ]
	line = f.readline()
rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

line = f.readline()
while not line == "":
	messages.append(line[:-1])
	line = f.readline()
f.close()

def getallmatch(text, option, rules):
	optmatches = [("", text)]
	for step in option:
		noptmatches = []
		for oldmatch in optmatches:
			for newmatch in lmatch(oldmatch[1], step, rules):
				noptmatches.append((oldmatch[0]+newmatch[0], newmatch[1]))
		optmatches = noptmatches
	return optmatches

def lmatch(text, rulenum, rules):
	rule = rules[rulenum]
	if isinstance(rule, str):
		if text.startswith(rule):
			return [(rule, text[len(rule):])]
		else:
			return []
	else:
		allmatches = []
		for option in rule:
			allmatches += getallmatch(text, option, rules)
		return allmatches

total = 0
for msg in messages:
	if any(x[1] == "" for x in lmatch(msg, 0, rules)):
		total += 1
print(total)