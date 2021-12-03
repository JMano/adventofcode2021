def parse_input(input):
    result = []
    for i in range(len(input)):
        result.append(input[i].split(' '))

    return result

def solve_part_1(input):
    position = 0
    depth = 0

    movements = parse_input(input)
    for movement in movements:
        match movement[0]:
            case "forward":
                position += int(movement[1])
            case "down":
                depth += int(movement[1])
            case "up":
                depth -= int(movement[1])

    print('Depth: ' + str(depth))
    print('Position: ' + str(position))
    print('Result: ' + str(position * depth))

def solve_part_2(input):
    position = 0
    depth = 0
    aim = 0

    movements = parse_input(input)
    for movement in movements:
        match movement[0]:
            case "forward":
                number = int(movement[1])
                position += number
                depth += aim * number
            case "down":
                aim += int(movement[1])
            case "up":
                aim -= int(movement[1])

    print('Aim: ' + str(aim))
    print('Depth: ' + str(depth))
    print('Position: ' + str(position))
    print('Result: ' + str(position * depth))

if __name__ == '__main__':
    with open('input.txt') as input:
        lines = input.read().split('\n')

    solve_part_1(lines)
    solve_part_2(lines)