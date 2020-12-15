def get_IDs(boarding_passes):
    seat_IDs = []
    for boarding_pass in boarding_passes:
        row, column = boarding_pass[:7], boarding_pass[7:]
        min_row, max_row = 0, 127
        min_col, max_col = 0, 7
        for i in row:
            half = (max_row - min_row) / 2
            if i == "F":
                max_row -= int(half) + 1
            elif i == "B":
                min_row += int(half) + 1
        for i in column:
            half = (max_col - min_col) / 2
            if i == "L":
                max_col -= int(half) + 1
            elif i == "R":
                min_col += int(half) + 1
        seat_IDs.append(min_row * 8 + min_col)
    return seat_IDs

def part1(boarding_passes):
    return max(get_IDs(boarding_passes))

def part2(boarding_passes):
    seat_IDs = sorted(get_IDs(boarding_passes))
    for i in range(len(seat_IDs) - 1):
        if seat_IDs[i + 1] != seat_IDs[i] + 1:
            return seat_IDs[i] + 1

def main():
    with open("inputs/day5.txt", "r") as f:
        boarding_passes = [i.rstrip() for i in f]
    print(f"highest seat ID: {part1(boarding_passes)}")
    print(f"my seat ID: {part2(boarding_passes)}")

main()
