from pathlib import Path
from typing import Dict, List


def read_file_to_string_list(path) -> List[int]:
    with open(path) as f:
        data = [line.strip() for line in f.readlines()]
    return data


def parse_lines(lines: List[str]):
    # input lines shaped like ['1-3', 'b:', 'cdefg']
    parsed_lines = [{
        'min': int(elem[0].split('-')[0]),
        'max': int(elem[0].split('-')[1]),
        'letter': elem[1][0],
        'password': elem[2]
    }
        for elem in [line.split() for line in lines]
    ]
    # output lines shaped like {'min': 1, 'min': 3, 'letter': 'a', 'password': 'abcde'}
    return parsed_lines


def validate_password_min_max(p_data: Dict):
    return p_data['min'] <= p_data['password'].count(p_data['letter']) <= p_data['max']


def validate_password_position(p_data: Dict):
    # found this cool xor operator ^
    return (p_data['password'][(p_data['min'] - 1)] == p_data['letter']) ^ (p_data['password'][p_data['max'] - 1] == p_data['letter'])


def main(data: List):
    passwords = parse_lines(data)

    validated_passwords_a = list(filter(validate_password_min_max, passwords))
    print(f'Part a: length of valid passwords: {len(validated_passwords_a)}')

    validated_passwords_b = list(filter(validate_password_position, passwords))
    print(f'Part b: length of valid passwords: {len(validated_passwords_b)}')


if __name__ == '__main__':
    # Config run
    IS_TEST = False

    DAY = 'd02'
    PART = 'a'
    REF = 'ref' if IS_TEST else 'input'

    DATA_FILE_NAME = f'{DAY}_{PART}_{REF}.txt'
    path = Path(__file__).parent.absolute() / 'data' / DATA_FILE_NAME

    data = read_file_to_string_list(path)

    main(data)
