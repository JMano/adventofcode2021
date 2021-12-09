def parse_input(input):
    return [int(x) for x in input[0].split(",")]

def nr_of_elements_after_x_days(initial_state: list[int], x):
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

    fish_80 = nr_of_elements_after_x_days(initial_state, 80)
    print(len(fish_80)) # 388419

def solve_part_2(input):
    print("part2")

if __name__ == '__main__':
    with open('Day06/test_input.txt') as input:
        lines = input.read().split('\n')

    solve_part_1(lines)
    solve_part_2(lines)