def detect_diff_chars(txt, n_chars):
    for i in range(len(txt) - n_chars):
        if len(set(txt[i : i + n_chars])) == n_chars:
            break
    return i + n_chars


# First puzzle ----------

with open("inputs/06.txt", "r") as f:
    res = detect_diff_chars(f.read(), 4)
    print(res)

# Second puzzle ----------

with open("inputs/06.txt", "r") as f:
    res = detect_diff_chars(f.read(), 14)
    print(res)
