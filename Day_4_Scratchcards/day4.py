import os
import re

def double_sequence(n):
    return 2 ** (n -1) if n > 0 else 0

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')
with open(file_path, 'r') as f:
    puzzle_input = f.readlines()

def part1(puzzle_input):
    sum_value = 0
    for line in puzzle_input:
        card = line.split(":")
        blah = card[0]
        game_number = (card[0]).split()[1]
        #print(game_number)
        # Remove the "Game ##: " portion
        numbers = card[1].split("|")
        win_nums = set(map(int, numbers[0].split()))
        player_nums = set(map(int, numbers[1].split()))
        intersection = win_nums.intersection(player_nums)
        num_matches = len(intersection)
        win_value = double_sequence(num_matches)
        sum_value += win_value
        #print (f"Game {game_number} matches: {matches} value= {win_value}.  running total = {sum_value}")
    return sum_value


def part2(puzzle_input):
    card_list = [1] * len(puzzle_input)
    for i, line in enumerate(puzzle_input):
        # numbers = line.split(":")[1].split("|")
        # win_nums = set(map(int, numbers[0].split()))
        # actual_nums = set(map(int, numbers[1].split()))
        win_nums, actual_nums = (set(map(int, part.split())) for part in line.split(":")[1].split("|"))
        wins = len(win_nums.intersection(actual_nums))
        print(f"Card[{i}]: Count={card_list[i]}  Wins={wins}")
        for j in range(wins):
            print(f"New Card[{i + j + 1}] = {card_list[i + j + 1]} + {card_list[i]}")
            card_list[i + j + 1] += card_list[i]
    return sum(card_list)

print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))



# online solution comparison
def part2_online(puzzle_input):
    lines = puzzle_input.split('\n')
    regex = r':(.*)\|(.*)'
    # parentheses for matching and capturing two groups.
    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        win_nums, actual_nums = re.findall(regex, line)[0]
        # set & set is the same as set.intersection(set)
        overlap = set(win_nums.split()) & set(actual_nums.split())
        for j in range(len(overlap)):
            cards[i+j+1] += cards[i]
    
    return sum(cards)