from itertools import combinations

def part1(numbers):
    for i in range(25, len(numbers)):
        preamble = numbers[i-25:i]
        pairs = list(combinations(preamble, 2))
        for pair in pairs:
            if numbers[i] == pair[0] + pair[1]:
                break
        else:
            return numbers[i]

def part2(numbers):
    invalid_number = part1(numbers)
    index_first = 0
    total = numbers[index_first]
    i = 1
    while i < len(numbers):
        if numbers[i] == invalid_number:
            continue
        if total == invalid_number:
            index_last = i - 1
            smallest, largest = min(numbers[index_first:index_last + 1]), max(numbers[index_first:index_last + 1])
            return smallest + largest
        elif total + numbers[i] <= invalid_number:
            total += numbers[i]
        else:
            index_first += 1
            total = numbers[index_first]
            i = index_first
        i += 1

def main():
    with open("inputs/day9.txt", "r") as f:
        numbers = [int(i.rstrip()) for i in f]
    print(f"first number that does not have this property: {part1(numbers)}")
    print(f"encryption weakness: {part2(numbers)}")

main()
