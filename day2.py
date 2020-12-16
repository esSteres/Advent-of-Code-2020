f = open("day2.txt", "r")
correctpasswds = 0
for line in f:
    dash = line.index("-")
    sp = line.index(" ")
    colon = line.index(":")
    low = int(line[:dash])
    high = int(line[dash+1:sp])
    letter = line[sp+1:colon]
    passwd = line[colon+1:]
    if (passwd[low] == letter) ^ (passwd[high] == letter):
        correctpasswds += 1

print(correctpasswds)
f.close()
