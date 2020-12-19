f = open("day18.txt", "r")

def nexttoken(line):
	parens = 0
	for i in range(len(line)):
		if line[i] == "(":
			parens += 1
		if line[i] == ")":
			parens -= 1
		if line[i].isspace() and parens == 0:
			return (line[:i], line[i+1:])
	return (line, "")

def tokenize(line):
	tokens = []
	(tok, line) = nexttoken(line)
	while not tok == "":
		if tok[0] == "(":
			tokens.append(tokenize(tok[1:-1]))
		else:
			tokens.append(tok)
		(tok, line) = nexttoken(line)
	return tokens

def treeify(tokens):
	if isinstance(tokens, str):
		return int(tokens)
	elif len(tokens) == 1:
		return treeify(tokens[0])
	return (treeify(tokens[:-2]), tokens[-2], treeify(tokens[-1]))

def compute(tree):
	if isinstance(tree, int):
		return tree
	elif tree[1] == "+":
		return compute(tree[0]) + compute(tree[2])
	else:
		return compute(tree[0]) * compute(tree[2])

total = 0
for line in f:
	total += compute(treeify(tokenize(line)))
print(total)