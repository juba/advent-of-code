from advent import Day

day = Day(10)

# First puzzle ---------


def solve1(file):
    values = [1]
    with open(file, "r") as f:
        for line in f:
            curr = values[-1]
            if line.startswith("noop"):
                values = values + [curr]
            if line.startswith("addx"):
                values = values + [curr, curr + int(line.split()[1])]
    return sum([values[i - 1] * i for i in [20, 60, 100, 140, 180, 220]])


print(solve1(day.test_file))
print(solve1(day.valid_file))


# Second puzzle ---------


def solve2(file):
    values = [1]
    with open(file, "r") as f:
        for line in f:
            curr = values[-1]
            if line.startswith("noop"):
                values = values + [curr]
            if line.startswith("addx"):
                values = values + [curr, curr + int(line.split()[1])]
    pixels = ""
    for i, val in enumerate(values):
        if (i % 40) + 1 in range(val, val + 3):
            pixels += "#"
        else:
            pixels += "."
    for i in range(6):
        print(pixels[i * 40 : (i + 1) * 40])


print(solve2(day.test_file))
print(solve2(day.valid_file))
