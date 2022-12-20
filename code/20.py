from advent.day import Day
import numpy as np

day = Day(20)


def solve(orig, n_mix=1):
    n = len(orig)
    # Transform values into (divider, rest tuples)
    a = list(
        map(
            lambda x: (x // (n - 1), x % (n - 1))
            if x >= 0
            else (-(-x // (n - 1)), -(-x % (n - 1))),
            orig,
        )
    )
    # Keep original positions movement
    a_positions = list(range(len(a)))
    for mix in range(n_mix):
        for i in range(len(a)):
            pos = a_positions.index(i)
            mul, item = a[pos]
            new_pos = pos + item
            if new_pos >= n:
                new_pos = new_pos % (n - 1)
            if new_pos <= -n:
                new_pos = -(-new_pos % (n - 1))
            del a[pos]
            a.insert(new_pos, (mul, item))
            a_positions.remove(i)
            a_positions.insert(new_pos, i)
    zero_pos = a.index((0, 0))
    indices = [(zero_pos + i) % n for i in (1000, 2000, 3000)]
    pos = [a[index][0] * (n - 1) + a[index][1] for index in indices]
    return pos, sum(pos)


# First puzzle ----------


def solve1(lines):
    orig = list(map(int, lines))
    return solve(orig)


print(solve1(day.test_lines))  # 3
print(solve1(day.valid_lines))  # 4914

# Second puzzle ----------


def solve2(lines):
    orig = list(map(lambda x: int(x) * 811589153, lines))
    return solve(orig, n_mix=10)


print(solve2(day.test_lines))  # 1623178306
print(solve2(day.valid_lines))  # 7973051839072
