import sys
import fileinput
import pprint


octopi: list[list[int]] = []
flash_count = 0


def main() -> int:
    global octopi
    global flash_count

    octopi_text = list( fileinput.input() )

    octopi = [
        [
            int(x) for x in y.rstrip()
        ]
        for y in octopi_text
    ]

    for i in range(100):
        cycle_octopi()

    pprint.pprint(octopi)
    print( f"Flashes = {flash_count}" )

    return 0


def cycle_octopi() -> None:

    global octopi
    global flash_count

    # first bump all energy levels by 1
    for row in range(len(octopi)):
        for column in range(len(octopi[row])):
            octopi[row][column] += 1

    # check for flashes
    for row in range(len(octopi)):
        for column in range(len(octopi[row])):
            check_flash(row, column, 0)     # increase


def check_flash(r: int, c: int, increment: int) -> None:

    global octopi
    global flash_count

    surrounding_octopi = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        # skip self!
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    )

    if r < 0 or r > len(octopi)-1:
        # out of bounds too high or too low
        return

    if c < 0 or c > len(octopi[r])-1:
        # out of bounds too far left or right
        return

    if octopi[r][c] != 0:
        # has not already flashed this round
        # first pass has increment 0, other passes will have increment 1 since
        # an adjacent octopus has flashed
        octopi[r][c] += increment

    # check for flash
    if octopi[r][c] > 9:
        # flash
        flash_count += 1
        octopi[r][c] = 0

        # bump adjacent octopi
        for delta in surrounding_octopi:
            check_flash(r+delta[0], c+delta[1], 1)


if __name__ == '__main__':
    sys.exit(main())
