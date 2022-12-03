from string import ascii_letters
from functools import reduce


def score(letter):
    return ascii_letters.index(letter) + 1


# First puzzle ------------------


def line_score(line):
    half_len = len(line) // 2
    letter = (set(line[:half_len]) & set(line[half_len:])).pop()
    return score(letter)


with open("inputs/03.txt", "r") as f:
    lines = f.read().split("\n")
    res = sum([line_score(line) for line in lines])
    print(res)


# Second puzzle -----------------


def group_score(group):
    return score(
        reduce(lambda group1, group2: set(group1) & set(group2), group).pop()
    )


with open("inputs/03.txt", "r") as f:
    txts = f.read().split("\n")
    groups = [txts[i * 3 : i * 3 + 3] for i in range(len(txts) // 3)]
    res = sum([group_score(group) for group in groups])
    print(res)
