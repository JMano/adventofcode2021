def invert_bits(string):
    inverse = ''
    for i in string:
        inverse += '1' if i == '0' else '0'

    return inverse

def most_and_least_frequent(input, bit_to_check):
    count_0 = 0
    count_1 = 0

    for report in input:
        if report[bit_to_check] == '1':
            count_1 += 1
        else:
            count_0 += 1

    if count_1 > count_0:
        return ('1', '0')
    if count_0 > count_1:
        return ('0', '1')

    return ('1', '0')

def solve_part_1(input):
    number_of_bits = len(input[0])
    counts = [0] * number_of_bits

    for i in range(number_of_bits):
        most, _ = most_and_least_frequent(input, i)
        counts[i] = most

    gama_bits = ''.join(counts)
    gama = int(gama_bits, 2)
    epsilon_bits = invert_bits(gama_bits)
    epsilon = int(epsilon_bits, 2)
    print('Gama bits: ' + gama_bits)
    print('Gama dec: ' + str(gama))
    print('Epsilon bits: ' + epsilon_bits)
    print('Epsilon dec: ' + str(epsilon))
    print()
    print('Power consumption: ' + str(gama * epsilon)) # 3958484

def solve_part_2(input):
    oxygen_input = input.copy()
    co2_input = input.copy()
    oxygen_bits = ''
    co2_bits = ''

    bit_to_check = 0
    while len(oxygen_input) > 1:
        most, _ = most_and_least_frequent(oxygen_input, bit_to_check)
        oxygen_input = [r for r in oxygen_input if r[bit_to_check] == most]
        bit_to_check += 1

    oxygen_bits = oxygen_input[0]

    bit_to_check = 0
    while len(co2_input) > 1:
        _, least = most_and_least_frequent(co2_input, bit_to_check)
        co2_input = [r for r in co2_input if r[bit_to_check] == least]
        bit_to_check += 1

    co2_bits = co2_input[0]

    oxygen = int(oxygen_bits, 2)
    co2 = int(co2_bits, 2)

    print('Oxygen bits: ' + oxygen_bits)
    print('Oxygen dec: ' + str(oxygen))
    print('CO2 bits: ' + co2_bits)
    print('CO2 dec: ' + str(co2))
    print()
    print('Life support rating: ' + str(oxygen * co2)) # 1613181

if __name__ == '__main__':
    with open('test_input.txt') as input:
        lines = input.read().split('\n')

    print("--- Part 1 ---")
    solve_part_1(lines)
    print()
    print("--- Part 2 ---")
    solve_part_2(lines)