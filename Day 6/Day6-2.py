def countGroupAnswers(group):
    allanswers = []
    for answer in group:
        allanswers.append(set(answer))

    return len(set.intersection(*allanswers))
    

with open("Day 6/input.txt") as f:
    data = f.read().split("\n\n")

groups = []
for i in data:
    groups.append(i.splitlines())

total = 0

for i in groups:
    total += countGroupAnswers(i)

print(total)

