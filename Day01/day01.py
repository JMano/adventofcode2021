def parse_input(input):
    result = []
    for i in range(len(input)):
        result.append(int(input[i]))

    return result

def solve_part_1(input):
    count = 0
    lines = parse_input(input)
    for i in range(1, len(lines)):
        if lines[i] > lines[i-1]:
            count += 1

    print(count)

def sum_last_3(i, input):
    return input[i] + input[i - 1] + input[i - 2]

def solve_part_2(input):
    count = 0
    lines = parse_input(input)
    for i in range(3, len(lines)):
        if sum_last_3(i, lines) > sum_last_3(i - 1, lines):
            count += 1

    print(count)

if __name__ == '__main__':
    with open('input.txt') as input:
        lines = input.read().split('\n')

    solve_part_1(lines)
    solve_part_2(lines)