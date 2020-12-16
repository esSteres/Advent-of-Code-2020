import functools as ft

def eestep(l, q):
	l.append(l[-2] - (q*l[-1]))

def eea(a, b):
	r = [a, b]
	s = [1, 0]
	t = [0, 1]
	while not r[-1] == 0:
		q = r[-2]//r[-1]
		eestep(r, q)
		eestep(s, q)
		eestep(t, q)
	return (s[-2], t[-2])

def crtstep (e1, e2):
	(a1, n1) = e1
	(a2, n2) = e2
	(m1, m2) = eea(n1, n2)
	a12 = (a1*m2*n2) + (a2*m1*n1)
	n12 = n1*n2
	return (a12 % n12, n12)

def crt(l):
	return ft.reduce(crtstep, l[1:], l[0])

f = open("day13.txt", "r")
start = int(f.readline())
raw = f.readline().split(",")
f.close()
routes = []
for i in range(len(raw)):
	if not raw[i] == "x":
		routes.append((-i, int(raw[i])))

(a, n) = crt(routes)
print(a, n)
print(a%n)