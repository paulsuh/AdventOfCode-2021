import sys
import fileinput
import collections
import statistics


def main() -> int:
    for line in fileinput.input():
        crabs_list = [
            int(x) for x in line.rstrip().split(",")
        ]

    med = statistics.median(crabs_list)
    print( med )

    print( sum( [abs(x-med) for x in crabs_list] ) )

    return 0


if __name__ == '__main__':
    sys.exit(main())
