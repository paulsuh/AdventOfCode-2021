import sys
import fileinput


def main() -> int:

    zero_counts = [0] * 12
    one_counts = [0] * 12

    for line in fileinput.input():
        # line[:-1] to trim off the trailing newline
        for current_bit in enumerate(line[:-1]):
            if current_bit[1] == "0":
                zero_counts[current_bit[0]] += 1
            else:
                one_counts[current_bit[0]] += 1

    gamma_rate = 0
    epsilon_rate = 0
    for bit_count_pair in zip(zero_counts, one_counts):
        if bit_count_pair[0] == bit_count_pair[1] == 0:
            # no more bits, all counts are zero
            break
        if bit_count_pair[0] > bit_count_pair[1]:
            # more zeroes than ones
            gamma_rate = gamma_rate << 1
            epsilon_rate = (epsilon_rate << 1) + 1
        else:
            # more ones than zeroes
            gamma_rate = (gamma_rate << 1) + 1
            epsilon_rate = epsilon_rate << 1

    print( f"Zero counts: {zero_counts}" )
    print( f"One counts: {one_counts}" )
    print( f"Gamma rate: {gamma_rate}" )
    print( f"Epsilon rate: {epsilon_rate}" )
    print( f"Power consumption: {gamma_rate*epsilon_rate}" )

    return 0


if __name__ == '__main__':
    sys.exit(main())
