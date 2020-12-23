def part1(data):
    earliest_timestamp = int(data[0])
    bus_IDs = []
    timestamps = {}
    minutes = {}
    for i in range(1, len(data)):
        if data[i] != "x":
            bus_id = int(data[i])
            bus_IDs.append(bus_id)
            timestamps[bus_id] = 0
    for bus_id in bus_IDs:
        while timestamps[bus_id] < earliest_timestamp:
            timestamps[bus_id] += bus_id
        minutes[bus_id] = timestamps[bus_id] - earliest_timestamp
    return min(minutes.values()) * min(minutes, key=minutes.get)

def part2(data):
    pass

def main():
    with open("inputs/day13.txt", "r") as f:
        data = [f.readline().rstrip()]
        data += f.readline().rstrip().split(",")
    print(f"ID of the earliest bus multiplied by the number of minutes: {part1(data)}")
    # print(f"answer: {part2(data)}")

main()
