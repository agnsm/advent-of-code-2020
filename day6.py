def part1(data):
    groups = [i.replace("\n", "") for i in data.split("\n\n")]
    counter = 0
    for group in groups:
        questions = []
        for answer in group:
            if answer not in questions:
                questions.append(answer)
        counter += len(questions)
    return counter

def part2(data):
    groups = [i.replace("\n", " ") for i in data.split("\n\n")]
    counter = 0
    for group in groups:
        answers = group.split(" ")
        guess = list(answers[0])
        questions = []
        people = len(answers)
        for g in guess:
            if group.count(g) == people:
                questions.append(g)
        counter += len(questions)
    return counter

def main():
    with open("inputs/day6.txt", "r") as f:
        data = f.read().rstrip()
    print(f"sum (questions to which anyone answered 'yes'): {part1(data)}")
    print(f"sum (questions to which everyone answered 'yes'): {part2(data)}")

main()
