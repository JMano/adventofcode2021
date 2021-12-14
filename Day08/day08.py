from enum import Flag, auto

def parse_input(input):
    return [[x.split(" | ")[0].split(" "), x.split(" | ")[1].split(" ")] for x in input]

def solve_part_1(input):
    parsed_entries = parse_input(input);

    count_1 = 0
    count_4 = 0
    count_7 = 0
    count_8 = 0

    for entry in parsed_entries:
        for segment in entry[1]:
            match len(segment):
                case 2:
                    count_1 += 1
                case 4:
                    count_4 += 1
                case 3:
                    count_7 += 1
                case 7:
                    count_8 += 1

    print(count_1 + count_4 + count_7 + count_8)

def solve_part_2(input):
    print("part2")

if __name__ == '__main__':
    with open('Day08/test_input.txt') as input:
        lines = input.read().split('\n')

    solve_part_1(lines)
    solve_part_2(lines)