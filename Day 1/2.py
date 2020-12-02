with open("Day 1/input1.txt") as f:
    data = f.read().splitlines()

for i in range(0,len(data)):
    for j in range(i+1,len(data)):
        for k in range(j+1,len(data)):
            if (int(data[i]) + int(data[j]) + int(data[k])) == 2020:
                print(int(data[i]) * int(data[j]) * int(data[k]))
                break