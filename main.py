import argparse
import importlib
import os
from shutil import copyfile
from get_input import get_input_for_day, get_day, get_test_input_for_day

def load_input(args):
    day = args.day

    if args.test:
        return get_test_input_for_day(day)
    else:
        with open('.session') as session_file:
            session = session_file.read()

        return get_input_for_day(session, day)

def create_files(day):
    directory = 'Day' + day
    file_path = directory + '/day' + day + '.py'

    if not os.path.exists(file_path):
        if not os.path.exists(directory):
            os.makedirs(directory)

        copyfile('template.py', file_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--day', help='Day of the challenge', default='1', required=False)
    parser.add_argument('-t', '--test', help='Use test input', default=False, action='store_true')
    args = parser.parse_args()
    day_arg = args.day
    day = get_day(day_arg)

    create_files(day)

    input = load_input(args)


    module = importlib.import_module('Day' + day + '.day' + day)

    if hasattr(module, 'solve_part_1'):
        print("--- Part 1 ---")
        module.solve_part_1(input)
    else:
        print("Part1 not solved")

    print()

    if hasattr(module, 'solve_part_2'):
        print("--- Part 2 ---")
        module.solve_part_2(input)
    else:
        print("Part2 not solved")