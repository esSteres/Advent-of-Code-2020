f = open("day1.txt", "r")
mask = [False for x in range(2020)]
for raw in f:
    val = int(raw)
    if mask[2020-val]:
        print(val * (2020-val))
    mask[val] = True

