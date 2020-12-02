from collections import Counter

def isValid(s):
    policyRange,policyChar,password = s.split(" ")
    policyRange = list(map(int, policyRange.split("-")))
    policyChar = policyChar[0]
    if Counter(password)[policyChar] in range(policyRange[0], policyRange[1] + 1):
        return True
    else:
        return False

with open("2/input1.txt") as f:
    data = f.read().splitlines()

total = 0
for l in data:
    if isValid(l):
        total += 1

print(total)