def part1(adapters):
    adapters = [0] + sorted(adapters) + [(max(adapters) + 3)]
    differences = [0, 0, 0, 0]
    for i in range(len(adapters) - 1):
        diff = adapters[i + 1] - adapters[i]
        differences[diff] += 1
    return differences[1] * differences[3]

def part2(adapters):
    adapters = sorted(adapters) + [(max(adapters) + 3)]
    combinations = dict()
    combinations[0] = 1
    for a in adapters:
        combinations[a] = combinations.get(a - 1, 0) + combinations.get(a - 2, 0) + combinations.get(a - 3, 0)
    return combinations[adapters[-1]]

def main():
    with open("inputs/day10.txt", "r") as f:
        adapters = [int(i.rstrip()) for i in f]
    print(f"number of 1-jolt differences multiplied by the number of 3-jolt differences: {part1(adapters)}")
    print(f"total number of distinct ways: {part2(adapters)}")

main()
