def invert_bits(string):
    inverse = ''
    for i in string:
        inverse += '1' if i == '0' else '0'

    return inverse

def solve_part_1(input):
    number_of_bits = len(input[0])
    counts = [0] * number_of_bits

    for report in input:
        for i in range(number_of_bits):
            if report[i] == '1':
                counts[i] += 1

    length = len(input)
    for i in range(number_of_bits):
        counts[i] = '1' if counts[i] > (length / 2) else '0'

    gama_bits = ''.join(counts)
    gama = int(gama_bits, 2)
    epsilon_bits = invert_bits(gama_bits)
    epsilon = int(epsilon_bits, 2)
    print('Gama bits: ' + gama_bits)
    print('Gama dec: ' + str(gama))
    print('Epsilon bits: ' + epsilon_bits)
    print('Epsilon dec: ' + str(epsilon))
    print()
    print('Power consumption: ' + str(gama * epsilon))

def solve_part_2(input):
    print("part2")

if __name__ == '__main__':
    with open('test_input.txt') as input:
        lines = input.read().split('\n')

    solve_part_1(lines)
    solve_part_2(lines)