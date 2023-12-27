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
        self.games = self.prepare_games()

    def prepare_games(self):
        stripped_lines = [re.sub(r'Game \d+: ', '', line) for line in self.input.lines]
        games = [game.split('; ') for game in stripped_lines]
        print(games)
        return games

    # @staticmethod
    # def load_draw(draw_str, previous_draw):
    #     # 0. Parse Game:
    #     #   - First separate by commas (',') and then by whitespace (' ')
    #     draw_elmts = draw_str.split(',')
    #     for elmt in draw_elmts:
    #         val, col = elmt.split()
    #         previous_draw[col] += int(val)
    #     return previous_draw

    @staticmethod
    def load_draw(draw_str):
        """
        Parse the draw, placing number of colours in dict
        :param draw_str: string containing colours and amounts of cubes
        :return: filled in dict that is the draw
        """
        draw = {}
        draw_elmts = draw_str.split(',')
        for elmt in draw_elmts:
            val, col = elmt.split()
            draw[col] = int(val)
        return draw

    # @staticmethod
    def check_draw(self, draw):
        """
        Checks for each colour in the draw if it's a possible draw by comparing
        :param draw: dict, current draw to be checked
        :return: True or False value whether draw is possible
        """
        for col in draw:
            print(col, draw[col])
            if draw[col] > self.bag_content[col]:
                return False
        return True

    def check_game(self, game):
        """
        Go through all draws in the game and check if they are possible
        :param game: list of draws
        :return: return True or False if game is admissible
        """
        for draw_str in game:
            draw = self.load_draw(draw_str)
            if not self.check_draw(draw):
                return False
        return True

    def run_part1(self):
        i = 1
        id = 0
        for game in self.games:
            print(i, game)
            if self.check_game(game):
                id += i
                print(id)
            i += 1
        print(id)

    @staticmethod
    def find_min_set(game):
        """
        Find the minimum vals over a whole game
        :param game: List of strings with draws
        :return: return the minium set for which all draws are possible
        """
        min_set = {'red': 0, 'green': 0, 'blue': 0}
        for draw_str in game:
            draw_elmts = draw_str.split(',')
            for elmt in draw_elmts:
                val, col = elmt.split()
                min_set[col] = max(int(val), min_set[col])
        return min_set

    def run_part2(self):
        id_sum = 0
        for game in self.games:
            game_id = 1
            min_set = Day2.find_min_set(game)
            for val in min_set.values():
                game_id *= val
            id_sum += game_id
        print (id_sum)
    #
    #     # 1. Check Draw:
    #     #   - If draw is impossible --> Flag or drop
    #     #   - If draw is possible, save the values for each color (maybe in a particular order?) in a dict or a list.
    #
    #     # 2. Check Next Draw:
    #     #   - Add the values to the previous values and check the composite draw



if __name__ == '__main__':
    day2 = Day2()
    # day2.run_part1()
    day2.run_part2()