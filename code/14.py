from advent import Day

day = Day(14)


def build_space(lines):
    rocks = []
    void = []
    for line in lines:
        points = line.split(" -> ")
        for i in range(len(points) - 1):
            x0, y0 = map(int, points[i].split(","))
            x1, y1 = map(int, points[i + 1].split(","))
            for x in range(min(x0, x1), max(x0, x1) + 1):
                for y in range(min(y0, y1), max(y0, y1) + 1):
                    rocks.append(complex(x, y))
    min_x = min(map(lambda x: int(x.real), rocks))
    max_x = max(map(lambda x: int(x.real), rocks))
    max_y = max(map(lambda x: int(x.imag), rocks))
    for y in range(0, max_y + 1):
        void.append(complex(min_x - 1, y))
        void.append(complex(max_x + 1, y))
    for x in range(min_x - 1, max_x + 2):
        void.append(complex(x, max_y + 1))
    return rocks, void


# First puzzle ----------


def move1_1(position, rocks, void):
    for new_pos in [position + 1j, position - 1 + 1j, position + 1 + 1j]:
        if new_pos in void:
            return 0
        if new_pos not in rocks:
            return new_pos
    rocks.append(position)
    return position


def move_1(rocks, void):
    position = 500 + 0j
    while True:
        new_pos = move1_1(position, rocks, void)
        if new_pos == 0 or new_pos == 500 + 0j:
            return True
        if new_pos == position:
            return False
        position = new_pos


def solve1(file):
    rocks, void = build_space(open(file, "r").read().split("\n"))
    is_void = False
    count = 0
    while not is_void:
        count += 1
        is_void = move_1(rocks, void)
    return count - 1


print(solve1(day.test_file))
print(solve1(day.valid_file))


# Second puzzle ----------


def fill_pyramid(max_y, rocks):
    sands = [500 + 0j]
    for y in range(1, max_y + 1):
        for x in range(500 - y, 500 + y + 1):
            pos = complex(x, y)
            if (pos not in rocks) and (
                pos - 1j in sands
                or pos - 1j - 1 in sands
                or pos - 1j + 1 in sands
            ):
                sands.append(complex(x, y))
    return sands


def solve2(file):
    rocks, _ = build_space(open(file, "r").read().split("\n"))
    max_y = max(map(lambda x: int(x.imag), rocks)) + 1
    sands = fill_pyramid(max_y, rocks)
    return len(sands)


print(solve2(day.test_file))
print(solve2(day.valid_file))
