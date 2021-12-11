import sys
import fileinput
import functools


closing_stack = []
closing_char_dict = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

def main() -> int:

    global closing_char_dict
    global closing_stack

    scoring_dict = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    scores_list = []
    for line in fileinput.input():

        closing_stack = []
        try:
            remainder = line.rstrip()
            while len(remainder) > 0:
                next_close_char = closing_char_dict.get(remainder[0], None)
                remainder = dispatch_next_char(remainder[1:], next_close_char)

        except Exception as e:
            print(f"Corrupted line: {line} - Expected {e.args[0]}, but found {e.args[1]} instead.")

        else:
            print(f"closing stack = {''.join(closing_stack)}")
            line_score = functools.reduce(
                lambda score, char: score * 5 + scoring_dict[char],
                closing_stack,
                0
            )
            print(f"line_score = {line_score}")
            scores_list.append(line_score)

    print( f"Score = {sorted(scores_list)[len(scores_list)//2]}" )

    return 0


def dispatch_next_char( input: str, current_chunk_close: str ) -> (list[str], str):

    global closing_stack
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

    # made it all the way through,
    # append current_chunk_close to list
    # return empty string
    closing_stack.append(current_chunk_close)
    return ""


if __name__ == '__main__':
    sys.exit(main())
