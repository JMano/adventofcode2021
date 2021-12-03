import argparse
import importlib
from get_input import get_input_for_day, get_day

def get_day_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--day', help='Day')
    args = parser.parse_args()

    return args.day

def load_input():
    day = get_day_arg()

    with open('.session') as session_file:
        session = session_file.read()
    
    return get_input_for_day(session, day)


if __name__ == '__main__':
    input = load_input()
    day_arg = get_day_arg()
    day = get_day(day_arg)
    module = importlib.import_module('Day' + day + '.day' + day)
    module.solve_part_1(input)
    module.solve_part_2(input)