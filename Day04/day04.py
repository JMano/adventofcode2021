def parse_input(input):
    numbers = [int(n) for n in input[0].split(',')]
    boards = []

    for i in range(1, len(input), 6):
        boards.append([False, []])
        for row in input[i + 1:i + 6]:
            split_row = row.split()
            boards[-1][-1].append([])
            for v in split_row:
                boards[-1][1][-1].append([int(v), False])

    return (numbers, boards)

def has_won(board, number):
    has_number = False
    for i in range(len(board[1])):
        for j in range(len(board[1][i])):
            if number == board[1][i][j][0]:
                board[1][i][j][1] = True
                has_number = True
                break

    if not has_number:
        return False

    for row in range(len(board[1])):
        if all(board[1][row][col][1] for col in range(len(board[1][row]))):
            return True

    for col in range(len(board[1][0])):
        if all(board[1][row][col][1] for row in range(len(board[1]))):
            return True

    return False

def board_score(board):
    score = 0
    for row in range(len(board[1])):
        for col in range(len(board[1][row])):
            if not board[1][row][col][1]:
                score += board[1][row][col][0]

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
    numbers, boards = parse_input(input)

    last_won_board = None
    last_won_number = None
    all_boards_won = False
    for number in numbers:
        for i in range(len(boards)):
            won = has_won(boards[i], number)

            if won:
                boards[i][0] = True

                if all(board[0] for board in boards):
                    all_boards_won = True
                    last_won_board = boards[i]
                    last_won_number = number
                    break
            
            if all_boards_won:
                break

        if all_boards_won:
            break

    if all_boards_won:
        print(last_won_number * board_score(last_won_board))

if __name__ == '__main__':
    with open('Day04/test_input.txt') as input:
        lines = input.read().split('\n')

    solve_part_1(lines)
    solve_part_2(lines)