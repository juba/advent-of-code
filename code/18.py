from advent.day import Day
from itertools import combinations
from collections import deque, defaultdict
import numpy as np

day = Day(18)


def parse(input):
    return set(
        map(lambda x: tuple(map(int, x.split(","))), input.read().split("\n"))
    )


def connected(pair):
    p0, p1 = pair
    return sum(abs(p0[i] - p1[i]) for i in range(3)) == 1


def n_faces(cubes):
    pairs = combinations(cubes, 2)
    connexions = len([pair for pair in pairs if connected(pair)])
    faces = 6 * len(cubes) - 2 * connexions
    return faces


# First puzzle ----------


def solve1(input):
    cubes = parse(input)
    return n_faces(cubes)


print(solve1(day.test_input))
print(solve1(day.valid_input))  # 3610

# Second puzzle ----------


def bfs(connexions, start):
    queue = deque([start])
    marked = []
    while len(queue) > 0:
        pos = queue.pop()
        if pos in marked:
            continue
        marked.append(pos)
        for child in connexions[pos]:
            queue.appendleft(child)  # type: ignore
    return marked


def connexions_list(d):
    connexions = defaultdict(list)
    for start, end in combinations(d, 2):
        if connected((start, end)):
            connexions[start].append(end)
            connexions[end].append(start)
    return connexions


def solve2(input):
    cubes = parse(input)
    # FIXME don't use numpy just for that
    xmin, ymin, zmin = np.min(np.array(list(cubes)), axis=0) - 1
    xmax, ymax, zmax = np.max(np.array(list(cubes)), axis=0) + 1
    empty = set(
        (x, y, z)
        for x in range(xmin, xmax + 1)
        for y in range(ymin, ymax + 1)
        for z in range(zmin, zmax + 1)
    ).difference(cubes)
    connexions = connexions_list(empty)
    outside = bfs(connexions, (0, 0, 0))
    inside = empty.difference(outside)
    cubes = cubes.union(inside)
    return n_faces(cubes)


print(solve2(day.test_input))  # 58
print(solve2(day.valid_input))  # 2082
