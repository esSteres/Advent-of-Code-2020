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

line = f.readline()
while not line == "":
	messages.append(line[:-1])
	line = f.readline()
f.close()

def lmatch(text, rulenum, rules):
	rule = rules[rulenum]
	if isinstance(rule, str):
		if text.startswith(rule):
			return (rule, text[len(rule):])
		else:
			return ("", text)
	else:
		for option in rule:
			fullmatch = ""
			rest = text
			for step in option:
				(match, rest) = lmatch(rest, step, rules)
				if match == "":
					fullmatch = ""
					break
				else:
					fullmatch += match
			if not fullmatch == "":
				return (fullmatch, rest)
		return ("", text)

total = 0
for msg in messages:
	if lmatch(msg, 0, rules)[1] == "":
		total += 1
print(total)