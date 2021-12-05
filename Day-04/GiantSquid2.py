import sys
import more_itertools


def check_for_bingo(one_table: list) -> bool:

    # check rows
    for i in range(0, 25, 5):
        if sum(one_table[i:i+5]) > 5000:
            return True

    # check columns
    for i in range(5):
        if sum(one_table[i:25:5]) > 5000:
            return True

    return False


def main() -> int:

    with open( sys.argv[1] ) as inputfile:
        # read in the first line and parse it into a list
        nums_drawn_list = [
            int(x) for x in inputfile.readline().rstrip().split(",")
        ]

        # read tables
        tables_list = [
            [
                int(one_item)
                for one_row in rows if len(one_row) > 1
                for one_item in one_row.split()
            ]
            for rows in iter(more_itertools.grouper(inputfile, 6))
        ]

    # run through until hit a bingo
    for drawn_number in nums_drawn_list:
        print(f"Number drawn = {drawn_number}")
        remaining_tables = []
        for one_table in tables_list:
            try:
                hit_index = one_table.index(drawn_number)
                one_table[hit_index] += 1000

                # since there was a hit, check for bingo
                if check_for_bingo(one_table):
                    print(f"Bingo, removing table = {one_table}")
                    # skip this table
                    continue

            except ValueError:
                # it's ok, no hit found
                pass

            # add the table to the next round
            remaining_tables.append(one_table)

        if len(remaining_tables) == 0:
            # found the last table
            print(f"Last table = {tables_list[0]}")
            print(f"Answer = {drawn_number * sum([x for x in tables_list[0] if x < 1000])}")
            return 0

        tables_list = remaining_tables

    return 0


if __name__ == '__main__':
    sys.exit(main())
