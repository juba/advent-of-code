from advent import Day
import re

day = Day(15)


def parse(line):
    co = list(map(int, re.findall(r"-?\d+", line)))
    s = complex(co[0], co[1])
    b = complex(co[2], co[3])
    dist = abs(s.real - b.real) + abs(s.imag - b.imag)
    return {"sensor": s, "beacon": b, "dist": dist}


def reduce_range(r1, r2):
    if r1[0] > r2[1] or r2[0] > r1[1]:
        return None
    return (min(r1[0], r2[0]), max(r1[1], r2[1]))


def reduce_ranges(ranges):
    changed = True
    while changed:
        changed = False
        for i in range(len(ranges) - 1):
            for j in range(i + 1, len(ranges)):
                if (res := reduce_range(ranges[i], ranges[j])) is not None:
                    changed = True
                    ranges[i] = res
                    del ranges[j]
                    break
            if changed:
                break
    return ranges


def get_no_beacons(measures, y):
    no_beacon = []
    for l in measures:
        width = l["dist"] - abs(y - l["sensor"].imag)
        if width >= 0:
            r = l["sensor"].real
            interv = (int(r - width), int(r + width))
            no_beacon.append(interv)
    return reduce_ranges(no_beacon)


# First puzzle ---------


def solve1(file, y_line):
    measures = list(map(parse, open(file, "r").read().split("\n")))
    no_beacon = get_no_beacons(measures, y_line)
    n_beacons = len(
        set(l["beacon"] for l in measures if l["beacon"].imag == y_line)
    )
    size = sum(map(lambda r: r[1] - r[0] + 1, no_beacon)) - n_beacons
    return size


solve1(day.test_file, y_line=10)
solve1(day.valid_file, y_line=2000000)


# Second puzzle ---------


def solve2(file, limit):
    measures = list(map(parse, open(file, "r").read().split("\n")))
    x = y = -1
    for y in range(0, limit + 1):
        if len(no_beacon := get_no_beacons(measures, y)) > 1:
            x = min(no_beacon[0].stop, no_beacon[1].stop)
            break
    if x == -1:
        return None
    return (x, y), x * 4000000 + y


solve2(day.test_file, limit=20)
solve2(day.valid_file, limit=4000000)  # 11796491041245
