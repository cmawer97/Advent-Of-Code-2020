import math

def getSeatID(row, column):
    return (row*8 + column)

def parseSeat(s):
    rows = 128
    columns = 8
    vposmax = rows
    vposmin = 0
    hposmax = columns
    hposmin = 0

    vChecks = int(math.log2(rows))
    hChecks = int(math.log2(columns))

    vpos_data = s[:vChecks]
    hpos_data = s[vChecks:]
    for i in range(0,vChecks):
        if vpos_data[i] == 'F':
            vposmax = vposmax - (2 ** (vChecks - 1 - i))
        elif vpos_data[i] == 'B':
            vposmin = vposmin + (2 ** (vChecks - 1 - i))

    for i in range(0,hChecks):
        if hpos_data[i] == 'L':
            hposmax = hposmax - (2 ** (hChecks - 1 - i))
        elif hpos_data[i] == 'R':
            hposmin = hposmin + (2 ** (hChecks - 1 - i))

    return vposmin, hposmin

with open("Day 5/input.txt") as f:
    data = f.read().splitlines()

maxSeatID = 0
for s in data:
    maxSeatID = max(getSeatID(*parseSeat(s)) , maxSeatID)

print(maxSeatID)
