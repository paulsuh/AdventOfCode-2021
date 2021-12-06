import sys
import fileinput
import functools


@functools.cache
def calc_growth( fish_timer: int, days_to_end: int ) -> int:
    # not enough time to reproduce
    if days_to_end < fish_timer+1:
        return 1

    return calc_growth( 6, days_to_end-(fish_timer+1) ) + calc_growth( 8, days_to_end-(fish_timer+1) )


def main() -> int:
    for line in fileinput.input():
        fish_list = [
            int(x) for x in line.rstrip().split(",")
        ]

    days_result = [
        calc_growth(x, 80) for x in range(7)
    ]

    print( sum(
        [
            days_result[x] for x in fish_list
        ]
    ))

    return 0


if __name__ == '__main__':
    sys.exit(main())
