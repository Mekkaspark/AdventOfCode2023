import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')
with open(file_path, 'r') as f:
    puzzle_input = f.readlines()

def part1(puzzle_input):
    total = 0
    for line in puzzle_input:
        total += 1
    return total

def part2(puzzle_input):
    total = 0
    for line in puzzle_input:
        total += 1
    return total

print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))