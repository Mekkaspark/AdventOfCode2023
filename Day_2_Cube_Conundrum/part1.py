import os
import re

red_limit = 12
green_limit = 13
blue_limit = 14

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'input.txt')
with open(file_path, 'r') as file:

    game_sum = 0
    for line in file:
        game_number = int(re.search(r"Game (\d+):", line).group(1))
        #print("Game number:", game_number)

        # Remove the "Game ##: " portion
        line = line.split(": ", 1)[1]
        trials = line.split(';')

        red_max, green_max, blue_max = 0, 0, 0

        for i, trial in enumerate(trials):
            cubes = trial.split(",")
            for cube in cubes:
                cube = cube.strip()
                match = re.match(r"(\d+) (red|green|blue)", cube)
                if match:
                    count = int(match.group(1))
                    color = match.group(2)

                    if color == "red":
                        red_max = max(red_max, count)
                    elif color == "green":
                        green_max = max(green_max, count)
                    elif color == "blue":
                        blue_max = max(blue_max, count)

        print(f"Game {game_number}:  Red {red_max}, Green {green_max}, Blue {blue_max}")

        if (red_max > red_limit or green_max > green_limit or blue_max > blue_limit):
            # impossible game
            #print(f"Impossible Game: {game_number}")
            red_max = 0
        else:
            print(f"Valid Game: {game_number}")
            game_sum += game_number

    print(f"Sum of Possible Games: {game_sum}")
