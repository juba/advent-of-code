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
    max_y = max(map(lambda x: int(x.imag), rocks))
    return max_y, rocks


# First puzzle ----------


def move1(position, rocks):
    for new_pos in [position + 1j, position - 1 + 1j, position + 1 + 1j]:
        if new_pos not in rocks:
            return new_pos
    rocks.append(position)
    return position


def move(max_y, rocks):
    position = 500 + 0j
    while position.imag < max_y + 1:
        new_pos = move1(position, rocks)
        if new_pos == position:
            return False
        position = new_pos
    return True


def solve1(file):
    max_y, rocks = build_space(open(file, "r").read().split("\n"))
    is_void = False
    count = 0
    while not is_void:
        count += 1
        is_void = move(max_y, rocks)
    return count - 1


print(solve1(day.test_file))  # 24
print(solve1(day.valid_file))  # 674


# Second puzzle ----------


def fill_pyramid(max_y, rocks):
    sands = [500 + 0j]
    for y in range(1, max_y + 2):
        for x in range(500 - y, 500 + y + 1):
            pos = complex(x, y)
            if (pos not in rocks) and (
                pos - 1j in sands
                or pos - 1j - 1 in sands
                or pos - 1j + 1 in sands
            ):
                sands.append(pos)
    return sands


def solve2(file):
    max_y, rocks = build_space(open(file, "r").read().split("\n"))
    sands = fill_pyramid(max_y, rocks)
    return len(sands)


print(solve2(day.test_file))  # 93
print(solve2(day.valid_file))  # 24958
