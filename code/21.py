from advent.day import Day
from collections import deque
import numpy as np
import re

day = Day(21)

# First puzzle ----------


def parse(lines):
    numbers = {}
    statements = {}
    for line in lines:
        line = line.replace(":", "=")
        if match := re.findall(r"^(.+)= \d+$", line):
            numbers[match[0]] = line
        else:
            out, in1, in2 = re.findall(r"^(.+)= ([a-z]+) .* ([a-z]+)$", line)[
                0
            ]
            statements[out] = (out, in1, in2, line)

    return numbers, statements


def order(numbers, statements):
    queue = deque(statements.values())
    ok = list(numbers.keys())
    code = list(numbers.values())
    while len(queue) > 0:
        statement = queue.pop()
        if statement[1] in ok and statement[2] in ok:
            ok.append(statement[0])
            code.append(statement[3])
        else:
            queue.appendleft(statement)
    return code


def solve1(lines):
    numbers, statements = parse(lines)
    code = order(numbers, statements)
    exec("global root;" + ";".join(code))
    return eval("int(root)")


print(solve1(day.test_lines))
print(solve1(day.valid_lines))


# Second puzzle ----------


def solve2(lines):
    numbers, statements = parse(lines)
    numbers["humn"] = "humn = complex(0, 1)"
    _, child1, child2, _ = statements["root"]
    code = order(numbers, statements)
    exec(f"global {child1}, {child2};" + ";".join(code))
    diff = eval(child1) - eval(child2)
    return int(-(diff.real / diff.imag))


print(solve2(day.test_lines))
print(solve2(day.valid_lines))
