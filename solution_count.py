import math
from argparse import ArgumentParser

# A Horse on the Phonepad:
# Imagine you place a knight chess piece on a phone dial pad. This chess piece moves in an uppercase “L” shape:
# two steps horizontally followed by one vertically, or one step horizontally then two vertically:
#
#     * Pay no attention to the poorly-redacted star and pound keys.
#     * Suppose you dial keys on the keypad using only hops a knight can make.
#     * Every time the knight lands on a key, we dial that key and make another hop.
#     * The starting position counts as being dialed.
#
# Your mission:
#   Write a software that solves the following question:
#      * How many distinct numbers can you dial in N hops from a particular starting position?

S = None
N = None
counter = None


# Get the position of the dialed key.
def value_to_position(dialed_value):
    if dialed_value == 0:
        return [3, 1]
    elif 1 <= dialed_value <= 9:
        return [math.floor((dialed_value - 1) / 3), (dialed_value - 1) % 3]
    return None


def is_position_valid(dialed_positions):
    return all(-1 < el < 3 for el in dialed_positions) or dialed_positions == [3, 1]


# Find distinct numbers in a depth-first-search manner.
def DFS(dialed_position, hops):
    if hops == 0:
        global counter
        counter += 1
        return
    for vertical in (-2, -1, 1, 2):
        for horizontal in (-2, -1, 1, 2):
            if abs(horizontal) != abs(vertical):
                new_dialed_position = [dialed_position[0] + horizontal, dialed_position[1] + vertical]
                if is_position_valid(new_dialed_position):
                    DFS(new_dialed_position, hops - 1)


def run(starting_position, number_of_hops):
    global S, N, counter
    S = starting_position
    N = number_of_hops
    counter = 0

    DFS(value_to_position(S), N - 1)

    return counter


def argument_parser():
    try:
        parser = ArgumentParser()
        parser.add_argument('-S', '--starting_position', type=int, choices=range(0, 10), required=True)
        parser.add_argument('-N', '--number_of_hops', type=int, required=True)

        return parser.parse_args()
    except Exception as exp:
        print(exp)


if __name__ == '__main__':
    args = argument_parser()
    result = run(args.starting_position, args.number_of_hops)
    print("N (number of hops) = ", args.number_of_hops, ", S (starting position) = ", args.starting_position,
          ", D (# distinct numbers) = ", result)
