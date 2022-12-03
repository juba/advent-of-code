# First puzzle ----------

max_value = 0
cur_sum = 0

with open("inputs/01.txt") as f:
    for line in f:
        if line != "\n":
            cur_sum += int(line)
        else:
            if cur_sum > max_value:
                max_value = cur_sum
            cur_sum = 0

print(max_value)

# Second puzzle ----------

values = []
cur_sum = 0

with open("inputs/01.txt") as f:
    for line in f:
        if line != "\n":
            cur_sum += int(line)
        else:
            values.append(cur_sum)
            cur_sum = 0

values.sort(reverse=True)
print(sum(values[:3]))
