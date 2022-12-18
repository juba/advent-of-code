from advent.day import Day

day = Day(17)

# Pieces in (width, contour) format
pieces = [
    # Horizontal bar
    (
        4,
        (0j, 1 + 0j, 2 + 0j, 3 + 0j),
    ),
    # Plus
    (
        3,
        (1j, 1 + 0j, 1 + 2j, 2 + 1j),
    ),
    # Inversed L
    (
        3,
        (0j, 1 + 0j, 2 + 0j, 2 + 1j, 2 + 2j),
    ),
    # Vertical bar
    (1, (0j, 1j, 2j, 3j)),
    # Square
    (2, (0j, 1 + 0j, 0 + 1j, 1 + 1j)),
]

# First puzzle ---------


def solve1(file, n_pieces=2022, detect_cycle=False):
    jets = open(file, "r").read()
    rocks = set([0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j, 4 + 0j, 5 + 0j, 6 + 0j])
    combs = set()
    count = 0
    cycle_start = 0
    for i in range(n_pieces):
        # Cycle detection
        if detect_cycle:
            # FIXME This doesn't work in all cases. Must compute a cycle
            # of piece, move, and terrain features
            piece_move = (i % len(pieces), count % len(jets))
            if piece_move in combs:
                if cycle_start == 0:
                    cycle_start = i
                    combs = set()
                    combs.add((i % len(pieces), count % len(jets)))
                else:
                    cycle_length = i - cycle_start
                    return (cycle_start - cycle_length, cycle_length)
            else:
                combs.add((i % len(pieces), count % len(jets)))
        max_height = max(r.imag for r in rocks)
        position = complex(2, (max_height + 4))
        width, contour = pieces[i % len(pieces)]
        # print(contour)
        while True:
            new_hpos = position + (-1 if jets[count % len(jets)] == "<" else 1)
            count += 1
            if new_hpos.real >= 0 and (new_hpos.real + width - 1) <= 6:
                if not any([(new_hpos + c in rocks) for c in contour]):
                    position = new_hpos
            new_vpos = position - 1j
            if any([(new_vpos + c in rocks) for c in contour]):
                for c in contour:
                    rocks.add(position + c)
                break
            else:
                position = new_vpos
    return int(max(r.imag for r in rocks))


print(solve1(day.test_file))
print(solve1(day.valid_file))  # 3200

# Second puzzle ---------


def solve2(file, n_pieces=1000000000000):
    cycle_start, cycle_length = solve1(file, n_pieces=100000, detect_cycle=True)  # type: ignore
    print(f"Found cycle at {cycle_start}, length {cycle_length}")
    height_start = solve1(file, n_pieces=cycle_start)
    height_cycle = (
        solve1(file, n_pieces=cycle_start + cycle_length) - height_start
    )  # type: ignore
    n_cycles = (n_pieces - cycle_start) // cycle_length
    between_cycles_diff = (
        height_start
        + 2 * height_cycle
        - solve1(file, n_pieces=cycle_start + 2 * cycle_length)
    )
    print(f"Found between cycles diff of {between_cycles_diff}")
    end_cycles = (n_pieces - cycle_start) % cycle_length
    height_end = solve1(file, n_pieces=cycle_start + cycle_length + end_cycles) - height_start - height_cycle  # type: ignore
    height = (
        height_start
        + height_cycle * n_cycles
        + height_end
        - between_cycles_diff * (n_cycles - 1)
    )
    return height


print(solve2(day.test_file))
print(solve2(day.valid_file))  # 1584927536247
