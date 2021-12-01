import fileinput


depth_increasing_count: int = 0
previous_depth = -1
for line in fileinput.input():
    if int(line) > previous_depth:
        depth_increasing_count += 1
    previous_depth = int(line)

print(f"Number of depth increases = {depth_increasing_count-1}")
