class Bag:
	def __init__(self):
		self.parents = {}
		self.children = {}

bagGraph = {}
f = open("day7.txt", "r")
for line in f:
	(ruleSubject, part, ruleContents) = line.partition(" bags contain ")
	if not ruleSubject in bagGraph:
		bagGraph[ruleSubject] = Bag()

	rules = ruleContents.replace("bags", "bag")[:-6].split(" bag, ")
	for rule in rules:
		if rule == "no other": continue

		(num, part, bagType) = rule.partition(" ")
		if not bagType in bagGraph:
			bagGraph[bagType] = Bag()

		bagGraph[ruleSubject].children[bagType] = int(num)
		bagGraph[bagType].parents[ruleSubject] = int(num)

bagMemo = {}
def bagCount(bag):
	if bag in bagMemo:
		return bagMemo[bag]
	
	total = 0
	for child in bagGraph[bag].children:
		total += bagGraph[bag].children[child] * ( 1 + bagCount(child))
	bagMemo[bag] = total
	return total

print(bagCount("shiny gold"))