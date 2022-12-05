import pandas as pd
import numpy as np
import re
from copy import deepcopy

d = pd.read_fwf("inputs/05.txt", nrows=8, header=None, widths=[4] * 9).to_dict(
    orient="list"
)
d = {
    key: [val.strip("[]") for val in value if val is not np.nan][::-1]
    for key, value in d.items()
}

# First puzzle ----------

d1 = deepcopy(d)
with open("inputs/05.txt", "r") as f:
    for line in f.readlines()[10:]:
        n, fr, to = (int(x) for x in re.findall(r"\d+", line))
        values = d1[fr - 1][-n:]
        d1[fr - 1] = d1[fr - 1][:-n]
        d1[to - 1].extend(values[::-1])
    print("".join([values[-1] for values in d1.values()]))

# Second puzzle ----------

d2 = deepcopy(d)
with open("inputs/05.txt", "r") as f:
    for line in f.readlines()[10:]:
        n, fr, to = (int(x) for x in re.findall(r"\d+", line))
        values = d2[fr - 1][-n:]
        d2[fr - 1] = d2[fr - 1][:-n]
        d2[to - 1].extend(values)
    print("".join([values[-1] for values in d2.values()]))
