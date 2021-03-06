import sys
import fileinput


def main() -> int:
    seafloor_text = list(fileinput.input())
    seafloor = [
        [
            int(x) for x in y.rstrip()
        ]
        for y in seafloor_text
    ]

    low_points_list = []
    for row in range(len(seafloor)):
        for col in range(len(seafloor[row])):
            # compare cell above
            if seafloor[row][col] >= safe_locate_level(seafloor, col, row-1):
                continue
            # compare cell below
            if seafloor[row][col] >= safe_locate_level(seafloor, col, row+1):
                continue
            # compare cell left
            if seafloor[row][col] >= safe_locate_level(seafloor, col-1, row):
                continue
            # compare cell right
            if seafloor[row][col] >= safe_locate_level(seafloor, col+1, row):
                continue

            # cell is a low point
            low_points_list.append(seafloor[row][col])

    print(low_points_list)
    print( sum(low_points_list) + len(low_points_list) )

    return 0


def safe_locate_level(seafloor: [list[int]], column: int, row: int):
    if column < 0 or column > len(seafloor[0])-1 or row < 0 or row > len(seafloor)-1:
        return 9
    else:
        return seafloor[row][column]


if __name__ == '__main__':
    sys.exit(main())
