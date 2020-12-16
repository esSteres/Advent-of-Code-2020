def treesinslope(dx, dy):
    f = open("day3.txt", "r")
    x = 0
    trees = 0
    for count, row in enumerate(f, start = 0):
        if count % dy != 0:
            continue
        if row[x] == "#":
            trees += 1
        x += dx
        x %= len(row) - 1
    f.close()
    return trees

total = 1
for x, y in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    total *= treesinslope(x, y)
print(total)
