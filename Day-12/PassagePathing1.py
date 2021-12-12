import sys
import fileinput


graphs_dict: dict[str, set[str]] = {}
paths_list: list[list[str]] = []

def main() -> int:

    global graphs_dict
    global paths_list

    line: str

    for line in fileinput.input():
        nodes: list[str] = line.rstrip().split("-")
        set0 = graphs_dict.get(nodes[0], set())
        set0.add(nodes[1])
        graphs_dict[nodes[0]] = set0
        set1 = graphs_dict.get(nodes[1], set())
        set1.add(nodes[0])
        graphs_dict[nodes[1]] = set1

    traverse_node( [], "start" )

    print(graphs_dict)
    print(paths_list)
    print(len(paths_list))

    return 0


def traverse_node( path: list, current_node: str ):

    global graphs_dict
    global paths_list

    if current_node == "end":
        # reached the end, add this path to the list
        final_path = path.copy()
        final_path.append(current_node)
        paths_list.append(final_path)
        return

    if current_node.islower() and current_node in path:
        # reached a small cave that has already been visited
        return

    # recurse
    for one_node in graphs_dict[current_node]:
        new_path = path.copy()
        new_path.append(current_node)
        traverse_node( new_path, one_node )


if __name__ == '__main__':
    sys.exit(main())
