import sys
import fileinput
import collections


def interpret_line( input_line: str, counts: collections.Counter ):

    line_parts = input_line.rstrip().split('|')
    # read 10 patterns
    patterns = line_parts[0].split()
    # read 4 digits
    digits = line_parts[1].split()

    counts += collections.Counter([len(x) for x in digits])


def main() -> int:
    digit_len_counts = collections.Counter()
    for line in fileinput.input():
        interpret_line(line, digit_len_counts)

    print( sum([digit_len_counts[x] for x in (2, 3, 4, 7)]) )

    return 0


if __name__ == '__main__':
    sys.exit(main())
