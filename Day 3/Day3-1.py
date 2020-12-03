with open("Day 3/input.txt") as f:
    data = f.read().splitlines()

tobogganX = 0

stepX = 3
stepY = 1
treesHit = 0
for tobogganY in data:
    if tobogganY[tobogganX] == "#":
        #print("Tree hit!")
        treesHit += 1
    if tobogganY[tobogganX] == "#":
        tobogganY = tobogganY[:tobogganX] + 'X' + tobogganY[tobogganX + 1:]
    else:
        tobogganY = tobogganY[:tobogganX] + 'O' + tobogganY[tobogganX + 1:]
    print(tobogganY)
    tobogganX = (tobogganX + stepX) % len(tobogganY)

print(treesHit)
