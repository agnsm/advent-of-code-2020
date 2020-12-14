def part1(passwords):
    counter = 0
    for i in passwords:
        limit, letter, password = i.split(" ")
        lowest, highest = [int(n) for n in limit.split("-")]
        letter = letter[0]
        if highest >= password.count(letter) >= lowest:
            counter += 1
    return counter

def part2(passwords):
    counter = 0
    for i in passwords:
        limit, letter, password = i.split(" ")
        position1, position2 = [int(n) for n in limit.split("-")]
        letter = letter[0]
        if bool(password[position1 - 1] == letter) != bool(password[position2 - 1] == letter):
            counter += 1
    return counter

def main():
    with open("inputs/day2.txt", "r") as f:
        passwords = [i for i in f]
    print(f"valid passwords: {part1(passwords)}")
    print(f"valid passwords: {part2(passwords)}")

main()
