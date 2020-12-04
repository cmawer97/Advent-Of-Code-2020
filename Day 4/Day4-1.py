import re

def checkPassport(passport):
    if len(passport) < 7:
        return False
    elif len(passport) == 8:
        return True
    # Otherwise, length of passport is 7, so we check if the missing field is the optional CID
    for field in passport:
        if field[:3].lower() == "cid":
            return False
    return True

with open("Day 4/input.txt") as f:
    data = f.read().split("\n\n")

passports = []

for l in data:
    passports.append(re.split(r"([ ]|\n)",l)[::2])

total = 0
for p in passports:
    if checkPassport(p):
        total += 1

print(total)