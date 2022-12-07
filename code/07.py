"""Note: this code won't work if the commands given as input 
visit the same directory twice."""

import re

# First puzzle ----------


def process_line(line, sizes, path):
    match_cd = re.search(r"^\$ cd (.*)$", line)
    # If cd command
    if match_cd:
        new_path = match_cd.group(1)
        if new_path == "/":
            path = "/"
        elif new_path == "..":
            # Before going up one level, add current directory size to parent directory size
            old_path = path
            path = re.sub("/[^/]+/$", "/", path)
            sizes[path] += sizes[old_path]
        else:
            path = path + new_path + "/"
            sizes[path] = 0
    match_size = re.search(r"^(\d+) .*$", line)
    # If file size
    if match_size:
        sizes[path] += int(match_size.group(1))
    return (sizes, path)


sizes = {"/": 0}
path = "/"
with open("inputs/07.txt", "r") as f:
    for line in f:
        sizes, path = process_line(line, sizes, path)
    # Go back to / to correctly compute total size
    level = len(re.findall(r"/", path)) - 1
    for i in range(level):
        sizes, path = process_line("$ cd ..", sizes, path)

sum([size for size in sizes.values() if size <= 100000])

# Second puzzle ---------

to_free_up = 30000000 - (70000000 - sizes["/"])
min([size for size in sizes.values() if size >= to_free_up])
