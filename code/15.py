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
    if r1.start > r2.stop or r2.start > r1.stop:
        return None
    return range(min(r1.start, r2.start), max(r1.stop, r2.stop))


def reduce_ranges(ranges):
    changed = True
    while changed:
        changed = False
        for i in range(len(ranges) - 1):
            for j in range(i + 1, len(ranges)):
                if (res := reduce_range(ranges[i], ranges[j])) is not None:
                    changed = True
                    del ranges[i]
                    del ranges[j - 1]
                    ranges.append(res)
                    break
            if changed:
                break
    return ranges


def get_no_beacons(measures, y):
    no_beacon = []
    for l in measures:
        width = int(l["dist"] - abs(y - l["sensor"].imag))
        if width >= 0:
            r = int(l["sensor"].real)
            interv = range(r - width, r + width + 1)
            no_beacon.append(interv)
    return reduce_ranges(no_beacon)


# First puzzle ---------


def solve1(file, y_line):
    measures = map(parse, open(file, "r").read().split("\n"))
    no_beacon = get_no_beacons(measures, y_line)
    size = sum(map(lambda r: r.stop - r.start - 1, no_beacon))
    return size


print(solve1(day.test_file, y_line=10))
print(solve1(day.valid_file, y_line=2000000))


# Second puzzle ---------


def solve2(file, limit):
    measures = list(map(parse, open(file, "r").read().split("\n")))
    x = -1
    for y in range(limit + 1, 0, -1):
        if len(no_beacon := get_no_beacons(measures, y)) > 1:
            x = min(no_beacon[0].stop, no_beacon[1].stop)
            break
    if x == -1:
        return None
    return (x, y), x * 4000000 + y


print(solve2(day.test_file, limit=20))
print(solve2(day.valid_file, limit=4000000))  # 11796491041245
