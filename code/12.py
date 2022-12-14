from advent import Day
from collections import deque
import re

day = Day(12)


class Grille:
    def __init__(self, txt):
        start_index = txt.find("S")
        end_index = txt.find("E")
        txt = txt.split("\n")
        self.height = len(txt)
        self.width = len(txt[0])
        self.start = [
            start_index % (self.width + 1),
            start_index // (self.width + 1),
        ]
        self.end = [
            end_index % (self.width + 1),
            end_index // (self.width + 1),
        ]
        self.grille = [[ord(c) for c in line] for line in txt]
        self.grille[self.start[1]][self.start[0]] = 96
        self.grille[self.end[1]][self.end[0]] = 123

    def add_neighbor(self, neighb, x0, y0, x1, y1):
        if x1 >= 0 and y1 >= 0 and x1 < self.width and y1 < self.height:
            if (self.grille[y1][x1] - self.grille[y0][x0]) <= 1:
                neighb.append([x1, y1])

    def get_neighbors(self, x, y):
        neighb = []
        self.add_neighbor(neighb, x, y, x + 1, y)
        self.add_neighbor(neighb, x, y, x, y + 1)
        self.add_neighbor(neighb, x, y, x - 1, y)
        self.add_neighbor(neighb, x, y, x, y - 1)
        return neighb


def bfs(grille, start=None):
    if start is None:
        start = grille.start
    queue = deque([(0, start)])
    marked = []
    while len(queue) > 0:
        length, node = queue.pop()
        if node == [grille.end[0], grille.end[1]]:
            return length
        if node in marked:
            continue
        marked.append(node)
        for neighb in grille.get_neighbors(node[0], node[1]):
            queue.appendleft([length + 1, neighb])  # type: ignore


# First puzzle ----------


def solve1(file):
    txt = open(file, "r").read()
    grille = Grille(txt)
    return bfs(grille)


print(solve1(day.test_file))
print(solve1(day.valid_file))


# Second puzzle ----------


def solve2(file):
    txt = open(file, "r").read()
    grille = Grille(txt)
    starts = [
        [find.start() % (grille.width + 1), find.start() // (grille.width + 1)]
        for find in re.finditer(r"[aS]", txt)
    ]
    lengths = [bfs(grille, start) for start in starts]
    lengths = [length for length in lengths if length is not None]
    return min(lengths)


print(solve2(day.test_file))
print(solve2(day.valid_file))
