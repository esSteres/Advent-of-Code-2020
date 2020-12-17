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


f.readline()
ownTicket = [int(x) for x in f.readline()[:-1].split(",")]
for i in range(3):
	line = f.readline()

tickets = []
while not line == "":
	tickets.append([int(x) for x in line[:-1].split(",")])
	line = f.readline()
f.close()

def qualifyingfields(val, pfields, allfields):
	qf = set()
	for field in pfields:
		if any(val in rng for rng in allfields[field]):
			qf.add(field)
	return qf

psets = [qualifyingfields(val, fields.keys(), fields) for val in ownTicket]
for ticket in tickets:
	newsets = []
	for i in range(len(ownTicket)):
		newset = qualifyingfields(ticket[i], psets[i], fields)
		if newset == set():
			break
		newsets.append(newset)

	if len(newsets) == len(ownTicket):
		psets = newsets

final = ["" for i in range(len(psets))]
while any(not x == set() for x in psets):
	for i in range(len(psets)):
		if len(psets[i]) == 1:
			final[i] = psets[i].pop()
			for pset in psets:
				pset.discard(final[i])
			break

total = 1
for i in range(len(final)):
	if "departure" in final[i]:
		total *= ownTicket[i]
print(total)


