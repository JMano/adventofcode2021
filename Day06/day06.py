from collections import defaultdict

def parse_input(input):
    return [int(x) for x in input[0].split(",")]

def nr_of_elements_after_x_days_part1(initial_state: list[int], x):
    elements = initial_state.copy()
    for _ in range(x):
        prev_list = elements.copy()
        for i in range(len(prev_list)):
            if prev_list[i] == 0:
                elements[i] = 6
                elements.append(8)
            else:
                elements[i] -= 1

    return elements

def solve_part_1(input):
    initial_state = parse_input(input)

    fish_80 = nr_of_elements_after_x_days_part1(initial_state, 80)
    print(len(fish_80)) # 388419

def nr_of_elements_after_x_days_part2(initial_state: list[int], x):
    elements = defaultdict(lambda: 0)
    for state in initial_state:
        elements[state] += 1

    for _ in range(x):
        new_elements = defaultdict(lambda: 0)
        for key in range(9):
            if key == 0:
                new_elements[6] = elements[key]
                new_elements[8] = elements[key]
            elif key == 6 or key == 8:
                new_elements[key - 1] = elements[key]
            else:
                new_elements[key - 1] += elements[key]

        elements = new_elements

    return elements

def solve_part_2(input):
    initial_state = parse_input(input)

    fish_256 = nr_of_elements_after_x_days_part2(initial_state, 256)
    print(sum(fish_256.values())) # 1740449478328 

if __name__ == '__main__':
    with open('Day06/test_input.txt') as input:
        lines = input.read().split('\n')

    solve_part_1(lines)
    solve_part_2(lines)