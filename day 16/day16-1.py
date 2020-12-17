f = open("day16.txt", "r")

fields = {}
line = f.readline()
while not line == "\n":
	(name, p, rawranges) = line[:-1].partition(": ")
	ranges = []

	for rawrange in rawranges.split(" or "):
		(low, p, high) = rawrange.partition("-")
		ranges.append(range(int(low), int(high)+1))

	fields[name] = ranges
	line = f.readline()

while not line == "nearby tickets:\n":
	line = f.readline()

tickets = []
line = f.readline()
while not line == "":
	tickets.append([int(x) for x in line[:-1].split(",")])
	line = f.readline()
f.close()

errtotal = 0
for ticket in tickets:
	for val in ticket:
		if not any(any(val in r for r in rs) for rs in fields.values()): # how is this allowed
			errtotal += val

print(errtotal) 