import sys
import fileinput
import collections


def interpret_line( patterns: list[str] ) -> dict[str, str]:

    # figure out which segments go where
    #
    #  1111
    # 2    3
    # 2    3
    #  4444
    # 5    6
    # 5    6
    #  7777
    #
    #
    # segment 1: 0, 2, 3, 5, 6, 7, 8, 9         8
    # segment 2: 0, 4, 5, 6, 8, 9               6
    # segment 3: 0, 1, 2, 3, 4, 7, 8, 9         8
    # segment 4: 2, 3, 4, 5, 6, 8, 9            7
    # segment 5: 0, 2, 6, 8                     4
    # segment 6: 0, 1, 3, 4, 5, 6, 7, 8, 9      9
    # segment 7: 0, 2, 3, 5, 6, 8, 9            7
    #
    # 0: 123567
    # 1: 36
    # 2: 13457
    # 3: 13467
    # 4: 2346
    # 5: 12467
    # 6: 124567
    # 7: 136
    # 8: 1234567
    # 9: 123467

    segment_counts = collections.Counter("".join(patterns))
    print(list(segment_counts.items()))

    segment_mapping = {}

    # uniquely identifiable segments
    # segment 5 is the only segment that appears in exactly 4 digits
    segment_5 = [x for x in segment_counts.items() if x[1] == 4][0]
    segment_mapping[segment_5[0]] = "5"
    segment_mapping["5"] = segment_5[0]

    # segment 2 is the only segment that appears in exactly 6 digits
    segment_2 = [x for x in segment_counts.items() if x[1] == 6][0]
    segment_mapping[segment_2[0]] = "2"
    segment_mapping["2"] = segment_2[0]

    # segment 6 is the only segment that appears in exactly 9 digits
    segment_6 = [x for x in segment_counts.items() if x[1] == 9][0]
    segment_mapping[segment_6[0]] = "6"
    segment_mapping["6"] = segment_6[0]

    # since we have identified segment 6, we can now identify segment 3, from numeral 1
    # numeral 1 = 3, 6
    numeral_1 = [x for x in patterns if len(x) == 2][0]
    segment_3 = [x for x in numeral_1 if x != segment_mapping["6"]]
    segment_mapping[segment_3[0]] = "3"
    segment_mapping["3"] = segment_3[0]

    # since we have segments 3 and 6, we can now identify segment 1, from numeral 7
    # numeral 7 = 1, 3, 6
    numeral_7 = [x for x in patterns if len(x) == 3][0]
    segment_1 = [x for x in numeral_7 if x not in numeral_1]
    segment_mapping[segment_1[0]] = "1"
    segment_mapping["1"] = segment_1[0]

    # 1 2 3 (4) 5 6 (7)
    # since we have segments 2, 3 and 6, we can now identify segment 4, from numeral 4
    # numeral 4 = 2, 3, 4, 6
    numeral_4 = [x for x in patterns if len(x) == 4][0]
    segment_4 = [x for x in numeral_4 if x not in (segment_mapping["2"], segment_mapping["3"], segment_mapping["6"] )]
    segment_mapping[segment_4[0]] = "4"
    segment_mapping["4"] = segment_4[0]

    # only segment 7 remains. Use numeral 8 to identify segment 7
    numeral_8 = [x for x in patterns if len(x) == 7][0]
    segment_7 = [x for x in numeral_8 if x not in segment_mapping.keys()]
    segment_mapping[segment_7[0]] = "7"
    segment_mapping["7"] = segment_7[0]

    return segment_mapping


def decode_line(segment_dict: dict[str, str], digits: list[str]) -> int:

    digits_dict = {
        "123567": "0",
        "36": "1",
        "13457": "2",
        "13467": "3",
        "2346": "4",
        "12467": "5",
        "124567": "6",
        "136": "7",
        "1234567": "8",
        "123467": "9"
    }

    return int("".join([
        digits_dict["".join(sorted([segment_dict[x] for x in one_digit]))]
        for one_digit
        in digits
    ]))


def split_line( input_line: str ) -> (list[str], list[str]):
    line_parts = input_line.rstrip().split('|')
    # read 10 patterns
    patterns = line_parts[0].split()
    # read 4 digits
    digits = line_parts[1].split()

    return patterns, digits


def main() -> int:

    result = 0
    for line in fileinput.input():
        patterns, digits = split_line(line)
        segment_dict = interpret_line(patterns)
        line_value = decode_line(segment_dict, digits)
        print(line_value)
        result += line_value

    print(result)

    return 0


if __name__ == '__main__':
    sys.exit(main())
