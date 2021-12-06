import sys
import fileinput
import functools


@functools.cache
def calc_growth( fish_timer: int, days_to_end: int ) -> int:
    # not enough time to reproduce
    if days_to_end < fish_timer:
        return 1

    return calc_growth( 7, days_to_end-fish_timer ) + calc_growth( 9, days_to_end-fish_timer )


def main() -> int:
    for line in fileinput.input():
        fish_list = [
            int(x) for x in line.rstrip().split(",")
        ]

    days_result = [
        calc_growth(x, 256) for x in range(1,8)
    ]

    print( sum(
        [
            days_result[x] for x in fish_list
        ]
    ))

    return 0


if __name__ == '__main__':
    sys.exit(main())
