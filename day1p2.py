f = open("day1.txt", "r")
mask = [0 for x in range(2020)]
vals = [int(x) for x in f]
f.close()

for val in vals:
    mask[val] = 1

for val in vals:
    target = 2020-val
    for test in vals:
        final = target-test
        if final > 0 and mask[final] == 1:
            print(val*test*(target-test))
            sys.exit()
    
