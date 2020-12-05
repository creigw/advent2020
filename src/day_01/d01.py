import logging
from pathlib import Path
from typing import List

# TODO globalize the logging init
logging.basicConfig()
log = logging.getLogger('d01')
log.setLevel(logging.INFO)


def read_file_to_int_list(path) -> List[int]:
    with open(path) as f:
        data = [int(line) for line in f]
    return data


def d1_a(data: List, seek_sum: int) -> int:
    """Primary logic for d1_a;

    Args:
        data (List): list of ints
        seek_sum (int): desired sum of 2 numbers

    Returns:
        int: product of the 2 numbers in the list that sum to the given seek_sum
    """
    return [x * y for x in data for y in data if x + y == seek_sum][0]


def d1_b(data: List, seek_sum: int) -> int:
    """Primary logic for d1_b;

    Args:
        data (List): list of ints
        seek_sum (int): desired sum of 3 numbers

    Returns:
        int: product of the 3 numbers in the list that sum to the given seek_sum
    """
    return [x * y * z for x in data for y in data for z in data if x + y + z == seek_sum][0]


def main(data: List):
    seek_sum = 2020
    result_a = d1_a(data, seek_sum)
    log.info("Result for d01_a:" + str(result_a))

    result_b = d1_b(data)
    log.info("Result for d01_b:" + str(result_b))


if __name__ == '__main__':
    REF_DATA_FILE_NAME = 'd01_a_ref.txt'
    DATA_FILE_NAME = 'd01_a_input.txt'

    path = Path(__file__).parent.absolute() / 'data' / DATA_FILE_NAME
    data = read_file_to_int_list(path)

    main(data)
