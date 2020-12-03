# Takes a list of strings representing a slope and the X/Y stepping of the toboggan, returns how many times the toboggan hits a tree
def findTreesHit(slope, stepX, stepY):
    treesHit = 0
    tobogganX = 0
    for tobogganY in slope[::stepY]:
        if tobogganY[tobogganX] == "#":
            treesHit += 1
        if tobogganY[tobogganX] == "#":
            tobogganY = tobogganY[:tobogganX] + 'X' + tobogganY[tobogganX + 1:]
        else:
            tobogganY = tobogganY[:tobogganX] + 'O' + tobogganY[tobogganX + 1:]
        print(tobogganY)
        tobogganX = (tobogganX + stepX) % len(tobogganY)
    return treesHit

with open("Day 3/input.txt") as f:
    data = f.read().splitlines()

total = findTreesHit(data,1,1) * findTreesHit(data,3,1) * findTreesHit(data,5,1) * findTreesHit(data,7,1) * findTreesHit(data,1,2)

print(total)
