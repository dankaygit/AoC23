import re
import os
from input_reader import InputReader


class Day2:

    def __init__(self):
        input_path = os.path.join(os.getcwd(), "input_files")
        filename = "day2.in"
        self.input = InputReader(os.path.join(input_path, filename))
        print(self.input.lines)

        self.bag_content = {'red': 12, 'green': 13, 'blue': 14}

    def prepare_games(self):
        stripped_lines = [re.sub(r'Game \d+: ', '', line) for line in self.input.lines]
        print(stripped_lines)
        games = [game.split('; ') for game in stripped_lines]
        print(games)
        return games


if __name__ == '__main__':
    day2 = Day2()
    day2.prepare_games()
