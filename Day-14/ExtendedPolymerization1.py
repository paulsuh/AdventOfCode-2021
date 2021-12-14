import sys
import fileinput
import more_itertools
import collections


patterns_dict: ((str, str), str) = {}


def main() -> int:

    global patterns_dict

    initial_template: str = None
    elements_set: set[str] = set()
    line: str

    for line in fileinput.input():

        if len(line.rstrip()) == 0:
            continue

        if initial_template is None:
            initial_template = line.rstrip()
            elements_set.update( set(initial_template) )
            continue

        # substitution rules
        pair, discard, insertion = line.rstrip().split()
        poly_result = pair[0]+insertion+pair[1]
        patterns_dict[(pair[0], pair[1])] = poly_result
        elements_set.update(set(pair))
        elements_set.add(insertion)

    print(patterns_dict)
    print(elements_set)

    current_polymer = initial_template
    for i in range(10):
        new_polymer = ""
        for one_pair in more_itertools.pairwise(current_polymer):
            new_polymer = new_polymer[:-1] + patterns_dict.get(one_pair, one_pair)
        current_polymer = new_polymer

    element_counts = collections.Counter(current_polymer)
    print(element_counts.most_common()[0][1]-element_counts.most_common()[-1][1])

    return 0


if __name__ == '__main__':
    sys.exit(main())
