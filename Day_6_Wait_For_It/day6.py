import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')
with open(file_path, 'r') as f:
    puzzle_input = f.readlines()

def calculate_max_distance(time, target):
    count = 0
    for i in range(time):
        d = i * (time-i)
        # print (f"Hold {i}: Distance= {d}")
        if d > target:
         count += 1
    return count

def calculate_max_distance2(time, target):
    min = 0
    max = time
    for i in range(time):
        d = i * (time - i)
        #print (f"Hold {i}: Distance= {d} bigger {target}")
        if d > target:
         min = i
         break;

    #for i in range(time, -1, -1):
    #    d = i * (time-i)
    #    if d > target:
    #     max = i
    #     break;

    count = time - min * 2 + 1
    print (f"Min {min}, Count = {count}")
    #print (f"Min {min}, Max {max}.  Count = {max-min + 1}")
    return count

def part1(puzzle_input):
    total = 1
    regex = r':(.*)'
    times = map(int, re.findall(regex, puzzle_input[0])[0].split())
    distances = map(int, re.findall(regex, puzzle_input[1])[0].split())
    for i, (time, distance) in enumerate(zip(times,distances)):
        # print(f"Index: {i}, Time: {time}ms, Distance: {distance}mm")
        total *= calculate_max_distance2(time, distance)

    return total

def part2(puzzle_input):
    total = 1
    regex = r':\s*(\d+(?:\s+\d+)*)'
    times = re.findall(regex, puzzle_input[0])[0].split()
    distances = re.findall(regex, puzzle_input[1])[0].split()
    time = int("".join(times))
    distance = int("".join(distances))
    print(f"Time: {time}ms, Distance: {distance}mm")
    total *= calculate_max_distance2(time, distance)
    return total;

print('Part 1:', part1(puzzle_input))
print('Part 2:', part2(puzzle_input))