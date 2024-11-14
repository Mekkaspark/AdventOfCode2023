import os
from itertools import permutations

sharedwords_to_number = {
    "oneight": "18", "twone": "21", "threeight": "38", "fiveight": "58",
    "sevenine": "79", "eightwo": "82", "eighthree": "83", "nineight": "98"
}

word_to_number = {
    "one": "1", "two": "2", "three": "3",
    "four": "4", "five": "5", "six": "6", "seven": "7",
    "eight": "8", "nine": "9"
}

number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def have_common_letter(word1, word2):
    return bool(set(word1) & set(word2))

def find_shared_middle_combinations(words):
    shared_combinations = []

    # Generate all unique pairs of words
    for word1, word2 in permutations(words, 2):
        for i in range(1, len(word1)):
            if word1[i:] == word2[:len(word1[i:])]:
                shared_combinations.append(word1 + word2)
                break
    return shared_combinations

combinations = find_shared_middle_combinations(number_words)
for combo in combinations:
    print(combo)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')
with open(file_path, 'r') as file:
    total_sum = 0

    for line in file:
        line = line.strip()
        for word, digit in sharedwords_to_number.items():
            line = line.replace(word, digit)
        for word, digit in word_to_number.items():
            line = line.replace(word, digit)

        digits = ''.join([char for char in line if char.isdigit()])

        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]
            two_digit_number = int(first_digit + last_digit)
            total_sum += two_digit_number
            #print(f"{two_digit_number}")
            #print(f"{two_digit_number}, Sum = {total_sum}")

    # Print sum
    print("Total Sum:", total_sum)
