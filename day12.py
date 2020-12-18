def part1(instructions):
    coordinates = {"N": 0, "S": 0, "E": 0, "W": 0}
    compass = ["N", "E", "S", "W"]
    direction = 1
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action == "F":
            coordinates[compass[direction]] += value
        elif action == "R":
            value //= 90
            direction = (direction + value) % len(compass)
        elif action == "L":
            value //= 90
            direction = (direction - value) % len(compass)
        else:
            coordinates[action] += value
    return abs(coordinates["N"] - coordinates["S"]) + abs(coordinates["E"] - coordinates["W"])

def part2(instructions):
    waypoint = {"X": 10, "Y": 1}
    coordinates = {"X": 0, "Y": 0}
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action == "N":
            waypoint["Y"] += value
        elif action == "S":
            waypoint["Y"] -= value
        elif action == "E":
            waypoint["X"] += value
        elif action == "W":
            waypoint["X"] -= value
        elif action == "F":
            coordinates["Y"] += waypoint["Y"] * value
            coordinates["X"] += waypoint["X"] * value
        elif action in ["L", "R"]:
            if action == "L":
                value = 360 - value
            if value == 90:
                waypoint = {"X": waypoint["Y"], "Y": -waypoint["X"]}
            elif value == 180:
                waypoint = {"X": -waypoint["X"], "Y": -waypoint["Y"]}
            elif value == 270:
                waypoint = {"X": -waypoint["Y"], "Y": waypoint["X"]}
    return abs(coordinates["X"]) + abs(coordinates["Y"])

def main():
    with open("inputs/day12.txt", "r") as f:
        instructions = [i.rstrip() for i in f]
    print(f"Manhattan distance: {part1(instructions)}")
    print(f"Manhattan distance: {part2(instructions)}")

main()
