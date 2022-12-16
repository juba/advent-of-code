from advent import Day
import re
from collections import deque
from itertools import combinations
from copy import deepcopy


day = Day(16)


def parse(file):
    passages = {}
    flows = {}
    for line in open(file, "r").read().split("\n"):
        id, flow, children = re.findall(
            r"Valve ([A-Z]{2}).*=(\d+);.*to valves? (.*)$", line
        )[0]
        passages[id] = children.split(", ")
        if int(flow) > 0 or id == "AA":
            flows[id] = int(flow)
    # Compute shortest distances between non-zero valves
    paths = [
        (start, end, bfs(passages, start, end))
        for start, end in combinations(sorted(flows.keys()), 2)
    ]
    paths = paths + [(end, start, dist) for (start, end, dist) in paths]
    # Convert to paths dictionary
    dpaths = {}
    for start, end, dist in paths:
        if start not in dpaths:
            dpaths[start] = [(end, dist, flows[end])]
        else:
            dpaths[start].append((end, dist, flows[end]))
    # Return paths dictionary and flows
    return dpaths, flows


def bfs(passages, start, end):
    queue = deque([(0, start)])
    marked = []
    while len(queue) > 0:
        length, pos = queue.pop()
        if pos == end:
            return length
        if pos in marked:
            continue
        marked.append(pos)
        for child in passages[pos]:
            queue.appendleft((length + 1, child))  # type: ignore


def max_remain(flows, visited, minutes):
    remain_flows = sorted(
        [v for k, v in flows.items() if k not in visited], reverse=True
    )
    return sum(
        [
            remain_flows[i] * (minutes - i * 2 - 1)
            for i in range(min(len(remain_flows), minutes))
        ]
    )


# First puzzle ---------


def solve1(file):
    dpaths, flows = parse(file)
    solutions = [
        {"visited": ["AA"], "pos": "AA", "pressure": 0, "minutes": 30}
    ]
    best_pressure = 0
    for i in range(0, len(flows) - 1):
        print(i)
        new_solutions = []
        for sol in solutions:
            pos = sol["pos"]
            possible_paths = [
                path for path in dpaths[pos] if path[0] not in sol["visited"]
            ]
            for path in possible_paths:
                minutes = sol["minutes"] - path[1] - 1
                if minutes <= 0:
                    continue
                pressure = sol["pressure"] + path[2] * minutes
                if pressure > best_pressure:
                    best_pressure = pressure
                visited = sol["visited"] + [path[0]]
                best_remain = max_remain(flows, visited, minutes)
                if best_remain <= (best_pressure - pressure):
                    continue
                new_solutions.append(
                    {
                        "visited": visited,
                        "pos": path[0],
                        "pressure": pressure,
                        "minutes": minutes,
                    }
                )

        solutions = new_solutions.copy()

    return best_pressure


solve1(day.test_file)
solve1(day.valid_file)

# Second puzzle ---------


def solve2(file):
    dpaths, flows = parse(file)
    solutions = [
        {
            "visited": ["AA"],
            "man": {"pos": "AA", "minutes": 26},
            "elephant": {"pos": "AA", "minutes": 26},
            "pressure": 0,
        }
    ]
    best_pressure = 0
    for i in range(0, (len(flows) - 1)):
        print(i)
        new_solutions = []
        for sol in solutions:
            for mov in ["man", "elephant"]:
                pos = sol[mov]["pos"]
                if i == 0 and mov == "man":
                    possible_paths = dpaths[pos][: len(dpaths[pos]) // 2]
                elif i == 0 and mov == "elephant":
                    possible_paths = dpaths[pos][len(dpaths[pos]) // 2 :]
                else:
                    possible_paths = [
                        path
                        for path in dpaths[pos]
                        if path[0] not in sol["visited"]
                    ]
                for path in possible_paths:
                    minutes = sol[mov]["minutes"] - path[1] - 1
                    if minutes <= 0:
                        continue
                    pressure = sol["pressure"] + path[2] * minutes
                    if pressure > best_pressure:
                        best_pressure = pressure
                    visited = sol["visited"] + [path[0]]
                    best_remain = max_remain(flows, visited, minutes)
                    if best_remain <= (best_pressure - pressure):
                        continue
                    new_solution = sol.copy()
                    new_solution["visited"] = visited
                    new_solution["pressure"] = pressure
                    new_solution[mov] = {"pos": path[0], "minutes": minutes}
                    new_solutions.append(new_solution)
        solutions = new_solutions.copy()

    return best_pressure


solve2(day.test_file)
solve2(day.valid_file)  # 2824
