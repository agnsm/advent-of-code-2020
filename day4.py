import re

global fields, eye_colors
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def get_passports(data):
    passport_str = [i.replace("\n", " ") for i in data.split("\n\n")]
    passport_dict = [dict(field.split(":") for field in passport.split(" ")) for passport in passport_str]
    return passport_dict

def validate(passport):
    validators = {
        "byr": validate_byr(passport["byr"]),
        "iyr": validate_iyr(passport["iyr"]),
        "eyr": validate_eyr(passport["eyr"]),
        "hgt": validate_hgt(passport["hgt"]),
        "hcl": validate_hcl(passport["hcl"]),
        "ecl": validate_ecl(passport["ecl"]),
        "pid": validate_pid(passport["pid"])
    }
    for key in passport.keys():
        if key != "cid":
            if not validators[key]:
                return False
    return True

def validate_byr(value):
    return re.match("^[0-9]{4}$", value) and 1920 <= int(value) <= 2002

def validate_iyr(value):
    return re.match("^[0-9]{4}$", value) and 2010 <= int(value) <= 2020

def validate_eyr(value):
    return re.match("^[0-9]{4}$", value) and 2020 <= int(value) <= 2030

def validate_hgt(value):
    return re.match("^[0-9]{3}cm$", value) and 150 <= int(value[:-2]) <= 193 or \
           re.match("^[0-9]{2}in$", value) and 59 <= int(value[:-2]) <= 76

def validate_hcl(value):
    return re.match("^#[0-9a-f]{6}$", value)

def validate_ecl(value):
    return value in eye_colors

def validate_pid(value):
    return re.match("^[0-9]{9}$", value)

def part1(data):
    passports = get_passports(data)
    counter = 0
    for passport in passports:
        if "cid" in passport and len(passport) == len(fields) or \
                "cid" not in passport and len(passport) == len(fields) - 1:
            counter += 1
    return counter

def part2(data):
    passports = get_passports(data)
    counter = 0
    for passport in passports:
        if "cid" in passport and len(passport) == len(fields) or \
                "cid" not in passport and len(passport) == len(fields) - 1:
            if validate(passport):
                counter += 1
    return counter

def main():
    with open("inputs/day4.txt", "r") as f:
        data = f.read().rstrip()
    get_passports(data)
    print(f"valid passports: {part1(data)}")
    print(f"valid passports: {part2(data)}")

main()
