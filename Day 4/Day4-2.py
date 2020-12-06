import re

def check_byr(s):
    if int(s[4:]) in range(1920,2003):
        return True
    else:
        print(s + " failed byr check")
        return False
        
def check_iyr(s):
    if int(s[4:]) in range(2010,2021):
        return True
    else:
        print(s + " failed iyr check")
        return False

def check_eyr(s):
    if int(s[4:]) in range(2020,2031):
        return True
    else:
        print(s + " failed eyr check")
        return False

def check_hgt(s):
    if s[-2:] == "cm":
        if int(s[4:-2]) in range(150,194):
            return True
        else:
            print(s + " failed hgt check (cm)")
            return False
    elif s[-2:] == "in":
        if int(s[4:-2]) in range(59,77):
            return True
        else:
            print(s + " failed hgt check (in)")
            return False
    else:
        print(s + " failed hgt check (no unit)")
        return False


def check_hcl(s):
    if s[4] == "#" and len(s[4:]) == 7:
        if bool(re.fullmatch(r"([a-f]|[0-9])+", s[5:])):
            return True
        else:
            print(s + " failed hcl check")
            return False
    print(s + " failed hcl check (invalid format)")
    return False

def check_ecl(s):
    if (s[4:] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        return True
    else:
        print(s + " failed ecl check")
        return False

def check_pid(s):
    if s[4:].isnumeric() and len(s[4:]) == 9:
        return True
    print(s + " failed pid check")
    return False
    

def checkPassport(passport):
    if len(passport) < 7:
        print("Passport is missing fields (less than 7)")
        return False
    elif len(passport) == 7:
        for field in passport:
            if field[:3].lower() == "cid":
                print("Passport is missing fields (7 with cid)")
                return False

    for field in passport:
        if field[:3] == "byr":
            if not check_byr(field):
                return False
        elif field[:3] == "iyr":
            if not check_iyr(field):
                return False
        elif field[:3] == "eyr":
            if not check_eyr(field):
                return False
        elif field[:3] == "hgt":
            if not check_hgt(field):
                return False
        elif field[:3] == "hcl":
            if not check_hcl(field):
                return False
        elif field[:3] == "ecl":
            if not check_ecl(field):
                return False
        elif field[:3] == "pid":
            if not check_pid(field):
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
    else:
        print(p)
        print()

print("Out of " + str(len(passports)) + " passports, " + str(total) + " are valid")