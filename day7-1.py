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

queue = {"shiny gold"}
visited = set()
while len(queue) > 0:
	nextBag = queue.pop()
	visited.add(nextBag)
	for bag in bagGraph[nextBag].parents:
		if not bag in visited:
			queue.add(bag)

visited.remove("shiny gold")
print(len(visited))