import numpy as np

d = np.genfromtxt("inputs/08.txt", dtype=np.int8, delimiter=1)


def apply_four_directions(f, d):
    """Apply f to d from, left, right, top and bottom directions."""
    return np.array(
        [
            np.apply_along_axis(f, 0, d),
            np.apply_along_axis(f, 1, d),
            np.flip(np.apply_along_axis(f, 0, np.flip(d, 0)), 0),
            np.flip(np.apply_along_axis(f, 1, np.flip(d, 1)), 1),
        ]
    )


# First puzzle ----------


def is_visible(v):
    max_values = np.roll(np.maximum.accumulate(v), shift=1)
    max_values[0] = -1
    return v > max_values


visible = np.logical_or.reduce(apply_four_directions(is_visible, d))
print(np.sum(visible))


# Second puzzle ----------


def count_visible(v):
    res = np.zeros(v.shape, dtype=np.int8)
    blocked = np.full(v.shape, False)
    heights = v.copy()
    heights[0] = 10000
    for i in np.arange(v.shape[0]):
        res[~blocked] += 1
        heights = np.roll(heights, shift=1)
        heights[0] = 10000
        blocked |= heights >= v
    res[0] = 0
    return res


n_visible = np.multiply.reduce(apply_four_directions(count_visible, d))
print(np.max(n_visible))
