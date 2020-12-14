def tree_count(area, right, down):
    counter = 0
    j = 0
    for i in range(0, len(area), down):
        if area[i][j] == "#":
            counter += 1
        j = (j + right) % len(area[0])
    return counter

def part1(area):
    return tree_count(area, 3, 1)

def part2(area):
    product = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for i in slopes:
        product *= tree_count(area, i[0], i[1])
    return product

def main():
    with open("inputs/day3.txt", "r") as f:
        area = [i.rstrip() for i in f]
    print(f"number of trees: {part1(area)}")
    print(f"number of trees multiplied together: {part2(area)}")

main()
