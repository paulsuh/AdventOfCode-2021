import sys
import fileinput


def main() -> int:

    scoring_dict = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    score = 0
    for line in fileinput.input():

        line = line.rstrip()
        try:
            if line[0] == "(":
                remainder = dispatch_next_char(line[1:], ")")
            elif line[0] == "[":
                remainder = dispatch_next_char(line[1:], "]")
            elif line[0] == "{":
                remainder = dispatch_next_char(line[1:], "}")
            elif line[0] == "<":
                remainder = dispatch_next_char(line[1:], ">")

        except Exception as e:
            print(f"Corrupted line: {line} - Expected {e.args[0]}, but found {e.args[1]} instead.")
            score += scoring_dict[e.args[1]]

    print( f"Score = {score}" )

    return 0


def group_parens( input: str ) -> str:

    # consume the open parens, then dispatch the next remainder
    remainder = dispatch_next_char(input[1:], ")")

    return remainder


def group_square_brackets( input: str ) -> str:

    # consume the open parens, then dispatch the next remainder
    remainder = dispatch_next_char(input[1:], "]")

    return remainder


def group_curly_brackets( input: str ) -> str:

    # consume the open parens, then dispatch the next remainder
    remainder = dispatch_next_char(input[1:], "}")

    return remainder


def group_angle_brackets( input: str ) -> str:

    # consume the open parens, then dispatch the next remainder
    remainder = dispatch_next_char(input[1:], ">")

    return remainder



def dispatch_next_char( input: str, current_chunk_close: str ) -> str:

    remainder = input

    while len(remainder) > 0:
        if remainder[0] == "(":
            remainder = group_parens(remainder)
        elif remainder[0] == "[":
            remainder = group_square_brackets(remainder)
        elif remainder[0] == "{":
            remainder = group_curly_brackets(remainder)
        elif remainder[0] == "<":
            remainder = group_angle_brackets(remainder)
        elif remainder[0] == current_chunk_close:
            remainder = remainder[1:]
            return remainder
        else:
            # bad close char
            raise Exception(current_chunk_close, remainder[0])

    return ""


if __name__ == '__main__':
    sys.exit(main())
