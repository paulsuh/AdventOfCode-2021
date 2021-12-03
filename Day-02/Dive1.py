import sys
import fileinput


def main() -> int:
    forward_position:int = 0
    depth:int = 0
    for line in fileinput.input():
        verb, magnitude = line.split()
        if verb == "down":
            depth += int(magnitude)
        elif verb == "up":
            depth -= int(magnitude)
        else:
            forward_position += int(magnitude)

    print(depth*forward_position)

    return 0


if __name__ == '__main__':
    sys.exit(main())
