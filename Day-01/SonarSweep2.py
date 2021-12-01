import fileinput
from more_itertools import sliding_window


depth_increasing_count: int = 0
previous_depth = -1
for measurements in sliding_window(fileinput.input(), 3):
    window_sum = sum([int(x) for x in measurements])
    if window_sum > previous_depth:
        depth_increasing_count += 1
    previous_depth = int(window_sum)

print(f"Number of depth increases = {depth_increasing_count-1}")
