import re

def inrange(f, low, high):
    try:
        x = int(f)
    except:
        return False
    return x >= low and x <= high

def inrangel(low, high):
    return lambda f: inrange(f, low, high)

reqfields = {
        "byr" : inrangel(1920, 2002),
        "iyr" : inrangel(2010, 2020),
        "eyr" : inrangel(2020, 2030),
        "hgt" : lambda f: inrange(f[:-2], 150, 193) if f[-2:] == "cm" else (inrange(f[:-2], 59, 76) if f[-2:] == "in" else False),
        "hcl" : lambda f: re.fullmatch("#[0-9a-f]{6}", f) != None,
        "ecl" : lambda f: f in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "pid" : lambda f: re.fullmatch("[0-9]{9}", f) != None
}

def isvalidpass(fields):
    out = True
    for elem, test in reqfields.items():
        if elem in fields:
            if not test(fields[elem]):
                out = False
        else:
            out = False
    return out

f = open("day4.txt", "r")
total = 0
fields = {}

for l in f:
    if l == "\n":
        if (isvalidpass(fields)):
            total += 1
        fields = {}
    else:
        for i in l[:-1].split(" "):
            fields[i[:3]] = i[4:]

if (isvalidpass(fields)):
    total += 1

print(total)
