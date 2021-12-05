def parse_input(input):
    numbers = [int(n) for n in input[0].split(',')]
    boards = []

    for i in range(1, len(input), 6):
        boards.append([])
        for row in input[i + 1:i + 6]:
            split_row = row.split()
            boards[-1].append([])
            for v in split_row:
                boards[-1][-1].append([int(v), False])

    return (numbers, boards)

def has_won(board, number):
    has_number = False
    for i in range(len(board)):
        for j in range(len(board[i])):
            if number == board[i][j][0]:
                board[i][j][1] = True
                has_number = True
                break

    if not has_number:
        return False

    for row in range(len(board)):
        if all(board[row][col][1] for col in range(len(board[row]))):
            return True, row

    for col in range(len(board[0])):
        if all(board[row][col][1] for row in range(len(board))):
            return True

    return False

def board_score(board):
    score = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if not board[row][col][1]:
                score += board[row][col][0]

    return score

def solve_part_1(input):
    numbers, boards = parse_input(input)

    for number in numbers:
        for i in range(len(boards)):
            won = has_won(boards[i], number)
            if won:
                break

        if won:
            break

    if won:
        print(number * board_score(boards[i]))

def solve_part_2(input):
    print("part2")

if __name__ == '__main__':
    with open('test_input.txt') as input:
        lines = input.read().split('\n')

    solve_part_1(lines)
    solve_part_2(lines)