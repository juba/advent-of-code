import pandas as pd


d = pd.read_fwf("inputs/02.txt", header=None, names=["V1", "V2"])

play_scores = {"X": 1, "Y": 2, "Z": 3}


# First puzzle ----------

play_result = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}

d = d.assign(
    score_play=d.V2.apply(lambda x: play_scores.get(x)),
    score_result=d.apply(lambda t: play_result.get(t.V1 + t.V2), axis=1),
    score_total=lambda x: x["score_play"] + x["score_result"],
)
res = d["score_total"].sum()
print(res)


# Second puzzle -------------

win_scores = {"X": 0, "Y": 3, "Z": 6}

play_comb = {
    "AX": "Z",
    "AY": "X",
    "AZ": "Y",
    "BX": "X",
    "BY": "Y",
    "BZ": "Z",
    "CX": "Y",
    "CY": "Z",
    "CZ": "X",
}

d = d.assign(
    score_win=d.V2.apply(lambda x: win_scores.get(x)),
    score_play=d.apply(
        lambda t: play_scores.get(play_comb.get(t.V1 + t.V2)), axis=1
    ),
    score_total=lambda x: x["score_play"] + x["score_win"],
)
res = d["score_total"].sum()
print(res)
