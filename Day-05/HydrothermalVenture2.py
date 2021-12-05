import sys
import fileinput
import re
import itertools


def main() -> int:

    all_lines = [
        [
            int(x) for x in
            re.split(",| -> ", one_line.rstrip())
        ]
        for one_line in fileinput.input()
    ]

    # Now determine overlaps
    # sparse matrix as dict
    vent_counts = {}
    for one_line in all_lines:
        if one_line[2] >= one_line[0]:
            # x is increasing
            x_range_start = one_line[0]
            x_range_end = one_line[2] + 1
            x_increment = 1
        else:
            # x is decreasing
            x_range_start = one_line[0]
            x_range_end = one_line[2] - 1
            x_increment = -1

        if one_line[3] >= one_line[1]:
            # y is increasing
            y_range_start = one_line[1]
            y_range_end = one_line[3] + 1
            y_increment = 1
        else:
            # y is decreasing
            y_range_start = one_line[1]
            y_range_end = one_line[3] - 1
            y_increment = -1

        # set fill value in case the line is horizontal or vertical
        if one_line[0] == one_line[2]:
            # vertical
            fill = one_line[0]
        elif one_line[1] == one_line[3]:
            # horizontal
            fill = one_line[1]
        else:
            # diagonal
            fill = None

        for one_coord in itertools.zip_longest(
                range(x_range_start, x_range_end, x_increment),
                range(y_range_start, y_range_end, y_increment),
                fillvalue=fill
        ):
            vent_counts[f"{one_coord[0]}+{one_coord[1]}"] = vent_counts.get(f"{one_coord[0]}+{one_coord[1]}", 0) + 1

    print(f"Number of overlaps is {len([x for x in vent_counts.values() if x > 1])}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
