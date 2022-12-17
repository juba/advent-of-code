from advent.day import Day
from functools import reduce
import re

day = Day(11)


def parse_group(txt):
    items = [
        int(item)
        for item in re.search(r"items: (.*)$", txt, re.MULTILINE)
        .group(1)
        .split(",")
    ]
    operation = re.search(r"new = (.*)$", txt, re.MULTILINE).group(1)
    div = int(re.search(r"divisible by (.*)$", txt, re.MULTILINE).group(1))
    true = int(re.search(r"true: .* monkey (\d)$", txt, re.MULTILINE).group(1))
    false = int(
        re.search(r"false: .* monkey (\d)$", txt, re.MULTILINE).group(1)
    )
    return {
        "items": items,
        "operation": operation,
        "div": div,
        "true": true,
        "false": false,
        "count": 0,
    }


# First puzzle ---------


def solve1(file):
    groups = open(file, "r").read().split("\n\n")
    monkeys = [parse_group(txt) for txt in groups]
    for i in range(20):
        for monkey in monkeys:
            items = [eval(monkey["operation"]) // 3 for old in monkey["items"]]
            for item in items:
                monkey["count"] += 1
                if item % monkey["div"] == 0:
                    monkeys[monkey["true"]]["items"].append(item)
                else:
                    monkeys[monkey["false"]]["items"].append(item)
            monkey["items"] = []
    counts = sorted([monkey["count"] for monkey in monkeys])
    return counts[-2] * counts[-1]


print(solve1(day.test_file))
print(solve1(day.valid_file))


# Second puzzle ---------


def solve2(file):
    groups = open(file, "r").read().split("\n\n")
    monkeys = [parse_group(txt) for txt in groups]
    mult_div = reduce(
        lambda x, y: x * y, [monkey["div"] for monkey in monkeys]
    )
    for i in range(10000):
        for monkey in monkeys:
            items = [eval(monkey["operation"]) for old in monkey["items"]]
            for item in items:
                monkey["count"] += 1
                if item % monkey["div"] == 0:
                    monkeys[monkey["true"]]["items"].append(item % mult_div)
                else:
                    monkeys[monkey["false"]]["items"].append(item % mult_div)
            monkey["items"] = []
    counts = sorted([monkey["count"] for monkey in monkeys])
    return counts[-2] * counts[-1]


print(solve2(day.test_file))
print(solve2(day.valid_file))
