from advent import Day
from itertools import zip_longest, starmap
from functools import cmp_to_key

day = Day(13)


def check_values(v1, v2):
    if v2 is None:
        return -1
    if v1 is None:
        return 1
    if isinstance(v1, int) and isinstance(v2, int):
        return v2 - v1
    elif isinstance(v1, int):
        return check_array(zip_longest([v1], v2))
    elif isinstance(v2, int):
        return check_array(zip_longest(v1, [v2]))
    else:
        return check_array(zip_longest(v1, v2))


def check_array(packet):
    for v1, v2 in packet:
        res = check_values(v1, v2)
        if res != 0:
            return res
    return 0


# First puzzle ----------


def solve1(file):
    lines = [
        eval(line) for line in open(file, "r").read().split("\n") if line != ""
    ]
    packets = starmap(zip_longest, zip(lines[0::2], lines[1::2]))
    indices = [
        i + 1 for i, packet in enumerate(packets) if check_array(packet) > 0
    ]
    return sum(indices)


print(solve1(day.test_file))
print(solve1(day.valid_file))


# Second puzzle ----------


def solve2(file):
    lines = [
        eval(line) for line in open(file, "r").read().split("\n") if line != ""
    ] + [[[2]], [[6]]]
    sorted_lines = sorted(
        lines, key=cmp_to_key(lambda x, y: -check_array(zip_longest(x, y)))
    )
    index2 = sorted_lines.index([[2]]) + 1
    index6 = sorted_lines.index([[6]]) + 1
    return index2 * index6


print(solve2(day.test_file))
print(solve2(day.valid_file))
