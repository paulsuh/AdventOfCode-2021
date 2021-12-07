import sys
import fileinput
import collections
import statistics


def main() -> int:
    for line in fileinput.input():
        crabs_list = [
            int(x) for x in line.rstrip().split(",")
        ]

    fuel_cost_list = [
        sum(
            [
                (abs(start_pos-dest_pos)*(abs(start_pos-dest_pos)+1))/2 for start_pos in crabs_list
            ]
        ) for dest_pos in range(max(crabs_list))
    ]

    print(fuel_cost_list)
    print(min(fuel_cost_list))

    mean = statistics.mean(crabs_list)
    print( mean )

    print( sum( [(abs(x-mean)*(abs(x-mean)+1))/2 for x in crabs_list] ) )

    return 0


if __name__ == '__main__':
    sys.exit(main())
