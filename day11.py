from copy import deepcopy

directions = [(-1, -1), (-1, 0), (-1, +1),
              (0, -1),            (0, +1),
              (+1, -1), (+1, 0), (+1, +1)]

def count(layout):
    counter = 0
    for i in layout:
        counter += i.count("#")
    return counter

def get_immediately_adjacent_seats(layout, i, j, row_len, col_len):
    occupied = 0
    for r, c in directions:
        if 0 <= i + r < row_len and 0 <= j + c < col_len:
            if layout[i + r][j + c] == "#":
                occupied += 1
    return occupied

def get_first_seats(layout, i, j, row_len, col_len):
    occupied = 0
    for row, col in directions:
        r, c = row, col
        while 0 <= i + r < row_len and 0 <= j + c < col_len:
            if layout[i + r][j + c] == "L":
                break
            if layout[i + r][j + c] == "#":
                occupied += 1
                break
            else:
                r += row
                c += col
    return occupied

def get_answer(layout, visible_occupied_seats, immediately_adjacent_seats):
    row_len = len(layout)
    col_len = len(layout[0])
    new_layout = deepcopy(layout)
    layout = []
    while layout != new_layout:
        layout = deepcopy(new_layout)
        for i in range(row_len):
            for j in range(col_len):
                if immediately_adjacent_seats:
                    occupied = get_immediately_adjacent_seats(layout, i, j, row_len, col_len)
                else:
                    occupied = get_first_seats(layout, i, j, row_len, col_len)
                if layout[i][j] == "L" and occupied == 0:
                    new_layout[i][j] = "#"
                elif layout[i][j] == "#" and occupied >= visible_occupied_seats:
                    new_layout[i][j] = "L"
    return count(layout)

def part1(layout):
    return get_answer(layout, 4, True)

def part2(layout):
    return get_answer(layout, 5, False)

def main():
    with open("inputs/day11.txt", "r") as f:
        layout = [list(i.rstrip()) for i in f]
    print(f"occupied seats: {part1(layout)}")
    print(f"occupied seats: {part2(layout)}")

main()
