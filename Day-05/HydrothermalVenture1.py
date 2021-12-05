import sys
import fileinput
import re


def main() -> int:

    all_lines = [
        [
            int(x) for x in
            re.split(",| -> ", one_line.rstrip())
        ]
        for one_line in fileinput.input()
    ]
    horizontal_lines = [
        one_line for one_line in all_lines
        if one_line[1] == one_line[3]
    ]
    vertical_lines = [
        one_line for one_line in all_lines
        if one_line[0] == one_line[2]
    ]

    # Now determine overlaps
    # sparse matrix as dict
    vent_counts = {}
    for one_line in horizontal_lines:
        # traverse the line
        for x_coord in range(min(one_line[0], one_line[2]), max(one_line[0], one_line[2])+1):
            vent_counts[f"{x_coord}+{one_line[1]}"] = vent_counts.get(f"{x_coord}+{one_line[1]}", 0) + 1
    for one_line in vertical_lines:
        # traverse the line
        for y_coord in range(min(one_line[1], one_line[3]), max(one_line[1], one_line[3])+1):
            vent_counts[f"{one_line[0]}+{y_coord}"] = vent_counts.get(f"{one_line[0]}+{y_coord}", 0) + 1

    print(f"Number of overlaps is {len([x for x in vent_counts.values() if x > 1])}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
