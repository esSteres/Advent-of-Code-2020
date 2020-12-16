f = open("day13.txt", "r")
start = int(f.readline())
routes = [int(x) for x in f.readline().split(",") if not x == "x"]
f.close()

def getroute(step, routes):
	for x in routes:
		if step % x == 0:
			return x
	return None

step = start
while getroute(step, routes) == None:
	step += 1

route = getroute(step, routes)

print("step:", step)
print("route:", route)
print((step-start)*route)