def get_bags1(rules, color):
    bags = []
    for rule in rules:
        if color in rule:
            index = rule.find("bags")
            bag = rule[:index].rstrip()
            if bag != color:
                bags.append(bag)
            rules.remove(rule)
    return bags

def part1(rules):
    bags = ["shiny gold"]
    counter = 0
    for bag in bags:
        new_bags = get_bags1(rules, bag)
        bags += new_bags
        counter += len(new_bags)
    return counter


def get_bags2(rules, color):
    bags = {}
    for rule in rules:
        if color in rule:
            index = rule.find(color)
            if index == 0:
                rule = rule.split(" ")
                for i in range(4, len(rule), 4):
                    if rule[i] != "no":
                        key = f"{rule[i+1]} {rule[i+2]}"
                        bags[key] = int(rule[i])
    return bags

def part2(rules):
    bags = {"shiny gold": 1}
    counter = 0
    while True:
        new_bags = {}
        for bag in bags:
            tmp_bags = get_bags2(rules, bag)
            for b in tmp_bags:
                tmp_bags[b] *= bags[bag]
                counter += tmp_bags[b]
                if b in new_bags:
                    new_bags[b] += tmp_bags[b]
                else:
                    new_bags[b] = tmp_bags[b]
        if len(new_bags) == 0:
            break
        else:
            bags = new_bags
    return counter

def main():
    with open("inputs/day7.txt", "r") as f:
        rules = [i.rstrip() for i in f]
    print(f"bag colors that contains at least one shiny gold bag: {part1(rules)}")
    with open("inputs/day7.txt", "r") as f:
        rules = [i.rstrip() for i in f]
    print(f"individual bags in one shiny gold bag: {part2(rules)}")

main()
