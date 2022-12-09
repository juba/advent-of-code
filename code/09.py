def move_head(h, movement):
    if movement == "L":
        h[0] -= 1
    if movement == "R":
        h[0] += 1
    if movement == "U":
        h[1] += 1
    if movement == "D":
        h[1] -= 1


# First puzzle ----------


def move_tail(h, t):
    diff_0 = h[0] - t[0]
    diff_1 = h[1] - t[1]
    if abs(diff_0) == 2:
        t[1] = h[1]
        t[0] += diff_0 // 2
    if abs(diff_1) == 2:
        t[0] = h[0]
        t[1] += diff_1 // 2


head = [0, 0]
tail = [0, 0]
tail_positions = []
with open("inputs/09.txt", "r") as f:
    for line in f:
        m, n = line.split(" ")
        for i in range(int(n)):
            move_head(head, m)
            move_tail(head, tail)
            if tail not in tail_positions:
                tail_positions.append(tail.copy())

print(len(tail_positions))


# Second puzzle ---------


def move_node(h, t):
    diff_0 = h[0] - t[0]
    diff_1 = h[1] - t[1]
    if (abs(diff_0) == 2) and (abs(diff_1) == 2):
        t[0] += diff_0 // 2
        t[1] += diff_1 // 2
    elif abs(diff_0) == 2:
        t[1] = h[1]
        t[0] += diff_0 // 2
    elif abs(diff_1) == 2:
        t[0] = h[0]
        t[1] += diff_1 // 2


nodes = [[0, 0] for i in range(10)]
tail_positions = []
with open("inputs/09.txt", "r") as f:
    for line in f:
        m, n = line.split(" ")
        for i in range(int(n)):
            move_head(nodes[0], m)
            for j in range(len(nodes) - 1):
                move_node(nodes[j], nodes[j + 1])
            if nodes[-1] not in tail_positions:
                tail_positions.append(nodes[-1].copy())

# print(tail_positions)
print(len(tail_positions))
