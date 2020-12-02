with open("1/input1.txt") as f:
    data = f.read().splitlines()

for i in range(0,len(data)):
    for j in range(i+1,len(data)):
        if (int(data[i]) + int(data[j]) == 2020):
            print(int(data[i]) * int(data[j]))
            break