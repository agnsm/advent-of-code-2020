def part1(report):
    for i in range(len(report)):
        for j in range(i + 1, len(report)):
            if report[i] + report[j] == 2020:
                print(f"{report[i]} * {report[j]} = {report[i] * report[j]}")

def part2(report):
    for i in range(len(report)):
        for j in range(i + 1, len(report)):
            for k in range(j + 1, len(report)):
                if report[i] + report[j] + report[k] == 2020:
                    print(f"{report[i]} * {report[j]} * {report[k]} = {report[i] * report[j] * report[k]}")

def main():
    with open("inputs/day1.txt", "r") as f:
        report = [int(i) for i in f]
    part1(report)
    part2(report)

main()
