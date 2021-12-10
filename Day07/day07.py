from collections import defaultdict

def parse_input(input):
    return [int(x) for x in input[0].split(",")]

def solve_part_1(input: list[int]):
    positions = parse_input(input)
    fuel_costs = defaultdict(lambda: 0)

    for position in positions:
        fuel_costs[position] = defaultdict(lambda: 0)

        for i in range(len(positions)):
            curr_position = positions[i]
            fuel_costs[position][curr_position] += abs(curr_position - position)

    costs = []
    for position in fuel_costs.keys():
        fuel_cost = sum(fuel_costs.get(position).values())
        print("Pos: " + str(position) + " | Fuel: " + str(fuel_cost))
        costs.append(fuel_cost)

    print("Min fuel: " + str(min(costs))) # 345035

def summation(start, finish):
    steps = abs(start - finish)
    return (steps * (steps + 1) / 2)

def solve_part_2(input):
    positions = parse_input(input)
    fuel_costs = defaultdict(lambda: 0)

    max_position = max(positions)

    for position in range(max_position):
        fuel_costs[position] = defaultdict(lambda: 0)

        for i in range(len(positions)):
            curr_position = positions[i]
            fuel_costs[position][curr_position] += summation(position, curr_position)

    costs = []
    for position in fuel_costs.keys():
        fuel_cost = sum(fuel_costs.get(position).values())
        print("Pos: " + str(position) + " | Fuel: " + str(fuel_cost))
        costs.append(fuel_cost)

    print("Min fuel: " + str(min(costs))) # 97038163

if __name__ == '__main__':
    with open('Day07/test_input.txt') as input:
        lines = input.read().split('\n')

    solve_part_1(lines)
    solve_part_2(lines)