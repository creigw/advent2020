from pathlib import Path
from typing import Dict, List
from functools import reduce

# [right, down]
PART_B_DIRECTIONS = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

PART_A_DIRECTION = PART_B_DIRECTIONS[1]


def read_file_to_string_list(path) -> List[int]:
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
    return data


def parse_lines(lines: List[str]) -> List[List[int]]:
    return [
        [0 if elem == '.' else 1 for elem in list(line)]
        for line in lines
    ]


class Position():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @property
    def position(self):
        return [self.x, self.y]

    def set_position(self, x, y):
        self.x = x
        self.y = y
        return self.position

    def move(self, x, y):
        self.x += x
        self.y += y
        return self.position


def traverse_map(tree_map, right_incr, down_incr):
    position = Position(0, 0)
    map_height = len(tree_map)
    map_width = len(tree_map[0])

    tree_count = 0
    while position.y < map_height:
        if position.x >= map_width:
            position.move(-map_width, 0)
        tree_count += tree_map[position.y][position.x]  # remember the matrix is [y], [x]
        position.move(right_incr, down_incr)

    return tree_count


def main(data: List):
    tree_map = parse_lines(data)

    # Part a
    tree_hits = traverse_map(tree_map, PART_A_DIRECTION[0], PART_A_DIRECTION[1])
    print(f'Number of trees hit (part a): {tree_hits}')

    # Part b
    tree_hits_product = reduce(lambda a, b: a * b, [traverse_map(tree_map, d[0], d[1]) for d in PART_B_DIRECTIONS])
    print(f'Number of trees hit product (part b): {tree_hits_product}')


if __name__ == '__main__':
    # Config run
    IS_TEST = False

    DAY = 'd03'
    PART = 'a'
    REF = 'ref' if IS_TEST else 'input'

    DATA_FILE_NAME = f'{DAY}_{PART}_{REF}.txt'
    path = Path(__file__).parent.absolute() / 'data' / DATA_FILE_NAME

    data = read_file_to_string_list(path)

    main(data)
