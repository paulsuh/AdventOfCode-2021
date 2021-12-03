import sys
import fileinput


def filter_common_high_bits(bit_values: str, nums: list[str], most_or_least_common: bool) -> (str, list):
    # most_or_least_common = True -- then select for most

    # otherwise, filter out list elements that don't have the value of bit_value
    # and determine which of zero or one is the most common in the next place
    # return filtered list of trimmed strings

    # filter out any value that don't start with the current prefix
    result_list: list[str] = [one_item for one_item in nums if one_item.startswith(bit_values)]

    if len(result_list) == 1:
        return bit_values, result_list

    # count ones in the next slot
    one_count: int = len(
        [one_item for one_item in result_list if one_item[len(bit_values)] == "1"]
    )
    zero_count: int = len(
        [one_item for one_item in result_list if one_item[len(bit_values)] == "0"]
    )

    if most_or_least_common:
        # looking for most common
        if one_count >= zero_count:
            return bit_values + "1", result_list
        else:
            return bit_values + "0", result_list
    else:
        # looking for least common
        if one_count < zero_count:
            return bit_values + "1", result_list
        else:
            return bit_values + "0", result_list


def main() -> int:
    nums_list = []
    for line in fileinput.input():
        # line[:-1] to trim off the trailing newline
        nums_list.append(line[:-1])

    max_list = nums_list
    bit_value = ""
    while len(max_list) > 1:
        bit_value, max_list = filter_common_high_bits(bit_value, max_list, True)

    print(f"Oxygen generator rating: {int(max_list[0], base=2)}")

    min_list = nums_list
    bit_value = ""
    while len(min_list) > 1:
        bit_value, min_list = filter_common_high_bits(bit_value, min_list, False)

    print(f"CO2 scrubber rating: {int(min_list[0], base=2)}")

    print(f"Life support rating: {int(max_list[0], base=2) * int(min_list[0], base=2)}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
