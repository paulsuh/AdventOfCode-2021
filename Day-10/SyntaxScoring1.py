import sys
import fileinput

closing_char_dict = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

def main() -> int:

    global closing_char_dict
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
            remainder = line
            while len(remainder) > 0:
                next_close_char = closing_char_dict.get(remainder[0], None)
                remainder = dispatch_next_char(remainder[1:], next_close_char)

        except Exception as e:
            print(f"Corrupted line: {line} - Expected {e.args[0]}, but found {e.args[1]} instead.")
            score += scoring_dict[e.args[1]]

    print( f"Score = {score}" )

    return 0


def dispatch_next_char( input: str, current_chunk_close: str ) -> str:

    global closing_char_dict
    remainder = input

    while len(remainder) > 0:

        if remainder[0] == current_chunk_close:
            # close out this chunk
            remainder = remainder[1:]
            return remainder

        next_close_char = closing_char_dict.get(remainder[0], None)
        if next_close_char is not None:
            remainder = dispatch_next_char(remainder[1:], next_close_char)
        else:
            # bad close char
            raise Exception(current_chunk_close, remainder[0])

    # made it all the way through, return empty string
    return ""


if __name__ == '__main__':
    sys.exit(main())
