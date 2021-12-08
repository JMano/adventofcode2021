class Line:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __repr__(self):
        return "(" + str(self.x1) + "," + str(self.y1) + ") -> (" + str(self.x2) + "," + str(self.y2) + ")"

def parse_input(input):
    coords = [x.split(" -> ") for x in input]
    lines: list[Line] = []
    max_x = 0
    max_y = 0
    for line in coords:
        start_point = line[0].split(",")
        end_point = line[1].split(",")
        x1 = int(start_point[0])
        y1 = int(start_point[1])
        x2 = int(end_point[0])
        y2 = int(end_point[1])

        if x1 > max_x:
            max_x = x1
        if x2 > max_x:
            max_x = x2
        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2

        lines.append(Line(x1, y1, x2, y2))

    return lines, max_x, max_y

def solve_part_1(input):
    lines, max_x, max_y = parse_input(input)
    report = [[0] * (max_x + 1) for _ in range(max_y + 1)]

    for line in lines:
        move_x = False
        move_y = False

        if line.x1 != line.x2 and line.y1 != line.y2:
            continue

        if line.x1 != line.x2:
            move_x = True
        else:
            move_y = True

        if move_x:
            for i in range(min(line.x1, line.x2), max(line.x1, line.x2) + 1):
                report[line.y1][i] += 1

        if move_y:
            for i in range(min(line.y1, line.y2), max(line.y1, line.y2) + 1):
                report[i][line.x1] += 1

    overlapping = 0
    for i in range(len(report)):
        for j in range(len(report[i])):
            if report[i][j] >= 2:
                overlapping += 1

    print(overlapping) # 5835

def solve_part_2(input):
    print("part2")

if __name__ == '__main__':
    with open('Day05/test_input.txt') as input:
        lines = input.read().split('\n')

    solve_part_1(lines)
    solve_part_2(lines)