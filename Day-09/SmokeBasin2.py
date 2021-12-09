import sys
import fileinput
from functools import cache


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
            low_points_list.append( (row, col) )

    basin_sizes = []
    for low_point in low_points_list:
        flood_points = []
        flood_basin(seafloor, flood_points, low_point[0], low_point[1] )
        basin_sizes.append( len(flood_points) )

    basin_sizes.sort(reverse=True)
    print( basin_sizes[0] * basin_sizes[1] * basin_sizes[2] )

    return 0


def safe_locate_level(seafloor: list[list[int]], column: int, row: int):
    if column < 0 or column > len(seafloor[0])-1 or row < 0 or row > len(seafloor)-1:
        return 9
    else:
        return seafloor[row][column]


def flood_basin( seafloor: list[list[int]], flood_points: list[tuple[int, int]], row: int, col: int ) -> None:

    if safe_locate_level(seafloor, col, row) == 9:
        return

    if (row, col) not in flood_points:
        flood_points.append((row, col))

        flood_basin( seafloor, flood_points, row-1, col )
        flood_basin( seafloor, flood_points, row+1, col )
        flood_basin( seafloor, flood_points, row, col-1 )
        flood_basin( seafloor, flood_points, row, col+1 )

    return


if __name__ == '__main__':
    sys.exit(main())
