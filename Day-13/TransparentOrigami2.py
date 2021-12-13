import sys
import fileinput
import re
import numpy as np


dots_list = []
folds_list = []


def main() -> int:

    global dots_list
    global folds_list
    line: str
    row_max: int = 0
    col_max: int = 0

    for line in fileinput.input():
        if len(line) == 1:
            continue
        elif line.startswith("fold along"):
            re_match = re.match( "fold along ([xy])=(\\d+)", line )
            folds_list.append( [re_match.group(1), int(re_match.group(2)) ] )
        else:
            # it's a point
            dots_strings = line.rstrip().split(",")
            dot_item = [ int(x) for x in dots_strings ]
            col_max = max( col_max, dot_item[0] )
            row_max = max( row_max, dot_item[1] )
            dots_list.append( dot_item )

    # convert to numpy 2d array
    base_array = np.zeros(
        (row_max+1, col_max+1),
        dtype=int
    )

    for dot in dots_list:
        base_array[dot[1]][dot[0]] = 1

    print(base_array)

    result_array = base_array
    for one_fold in folds_list:
        if one_fold[0] == "x":
            result_array = fold_vertical( result_array, one_fold[1] )
        else:
            result_array = fold_horizontal( result_array, one_fold[1] )

    np.set_printoptions(linewidth=100)
    print( result_array )

    return 0


def fold_horizontal( input_array: np.array, row: int ):

    # split by slicing
    top_array = input_array[:row]
    bottom_array = input_array[-1:row:-1]

    # max the two
    folded_array = np.maximum( top_array, bottom_array )

    return folded_array


def fold_vertical( input_array: np.array, col: int ):

    # split by slicing
    left_array = input_array[:, :col]
    right_array = input_array[:, -1:col:-1]

    # max the two
    folded_array = np.maximum( left_array, right_array )

    return folded_array


if __name__ == '__main__':
    sys.exit(main())
