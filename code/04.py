import re


# First puzzle -----------


def process_line(line):
    s1, e1, s2, e2 = map(int, line)
    return (s2 >= s1 and e2 <= e1) or (s1 >= s2 and e1 <= e2)


with open("inputs/04.txt", "r") as f:
    lines = f.read().splitlines()
    lines = [re.compile(r"[-,]").split(line) for line in lines]
    res = sum([process_line(line) for line in lines])
    print(res)


# Second puzzle -----------


def process_line(line):
    s1, e1, s2, e2 = map(int, line)
    return (s1 <= s2 and s2 <= e1) or (s1 >= s2 and s1 <= e2)


with open("inputs/04.txt", "r") as f:
    lines = f.read().splitlines()
    lines = [re.compile(r"[-,]").split(line) for line in lines]
    res = sum([process_line(line) for line in lines])
    print(res)
