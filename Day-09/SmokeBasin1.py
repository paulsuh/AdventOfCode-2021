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
    for i in range(len(seafloor)):
        for j in range(len(seafloor[i])):
            if i != 0:
                # compare cell above if not in top row
                if seafloor[i][j] >= seafloor[i-1][j]:
                    continue
            if i != len(seafloor)-1:
                # compare cell below if not in bottom row
                if seafloor[i][j] >= seafloor[i+1][j]:
                    continue
            if j != 0:
                # compare cell left if not in first column
                if seafloor[i][j] >= seafloor[i][j-1]:
                    continue
            if j != len(seafloor[i])-1:
                # compare cell right if not in last column
                if seafloor[i][j] >= seafloor[i][j+1]:
                    continue

            # cell is a low point
            low_points_list.append(seafloor[i][j])

    print(low_points_list)
    print( sum(low_points_list) + len(low_points_list) )

    return 0


if __name__ == '__main__':
    sys.exit(main())
