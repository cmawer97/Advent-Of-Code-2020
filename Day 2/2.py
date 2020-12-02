def isValid(s):
    policyRange,policyChar,password = s.split(" ")
    policyRange = list(map(int, policyRange.split("-")))
    policyChar = policyChar[0]

    if (password[policyRange[0] - 1] == policyChar) ^ (password[policyRange[1] - 1] == policyChar):
        return True

    else:
        return False

    

with open("Day 2/input1.txt") as f:
    data = f.read().splitlines()

total = 0
for l in data:
    if isValid(l):
        total += 1

print(total)