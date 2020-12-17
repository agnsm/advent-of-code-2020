def get_accumulator(instructions):
    i, accumulator = 0, 0
    visited = [False for i in instructions]
    while i < len(instructions) and not visited[i]:
        instruction = instructions[i]
        visited[i] = True
        operation, argument = instruction.split(" ")
        argument = int(argument)
        if operation == "acc":
            accumulator += argument
            i += 1
        elif operation == "jmp":
            i += argument
        else:
            i += 1
    if i == len(instructions):
        return True, accumulator
    else:
        return False, accumulator

def part1(instructions):
    return get_accumulator(instructions)[1]

def part2(instructions):
    for i in range(len(instructions)):
        operation, argument = instructions[i].split(" ")
        if operation == "acc":
            continue
        test = instructions.copy()
        if operation == "jmp":
            test[i] = f"nop {argument}"
        elif operation == "nop":
            test[i] = f"jmp {argument}"
        if get_accumulator(test)[0]:
            instructions = test
    return get_accumulator(instructions)[1]

def main():
    with open("inputs/day8.txt", "r") as f:
        instructions = [i.rstrip() for i in f]
    print(f"value of accumulator: {part1(instructions)}")
    print(f"value of accumulator after the program terminates: {part2(instructions)}")

main()
