import sys
import fileinput
import more_itertools
import collections
import functools


patterns_dict: ((str, str), list[str]) = {}


def main() -> int:

    global patterns_dict

    initial_template: list[str] = None
    line: str

    for line in fileinput.input():

        if len(line.rstrip()) == 0:
            continue

        if initial_template is None:
            initial_template = list(line.rstrip())
            continue

        # substitution rules
        pair, discard, insertion = line.rstrip().split()
        poly_result = [pair[0], insertion]
        patterns_dict[(pair[0], pair[1])] = poly_result

    element_counts = collections.Counter()
    for pair in more_itertools.pairwise(initial_template):
        element_counts += expand(pair[0], pair[1], 40)

    element_counts.update(initial_template[-1])

    print(element_counts.most_common())
    print(element_counts.most_common()[0][1]-element_counts.most_common()[-1][1])

    return 0


@functools.cache
def expand( e1: str, e2: str, depth: int ) -> collections.Counter:

    expansion = patterns_dict[(e1, e2)]
    if depth == 1:
        return collections.Counter(expansion)

    counts1 = expand( expansion[0], expansion[1], depth-1)
    counts2 = expand( expansion[1], e2, depth-1)

    return counts1+counts2


if __name__ == '__main__':
    sys.exit(main())
