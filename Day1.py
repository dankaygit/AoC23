import re
import os
import numpy as np
from input_reader import InputReader


class Day1:

    def __init__(self):
        input_path = os.path.join(os.getcwd(), "input_files")
        filename = "day1.in"
        self.input = InputReader(os.path.join(input_path, filename))
        print(self.input.lines)

        # Define a dictionary mapping spelled-out numbers to digits
        # There are three special cases of overlapping digits, which need separate treatment
        self.special_digits_mapping = {
            'oneight': '18', 'eightwo': '82', 'twone': '21'
        }

        self.spelled_digit_mapping = {
            'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
        }

    @staticmethod
    def extract_cal_val(line):
        """
        This function takes an input string and returns a value which contains the first and last digit from the string.
        :param line: string containing digits and other garbage
        :return: the integer made from the first and last digit in the string.
        """

        # Find all digits from string `line` and check if there is only one.
        # If there's only one it needs to be duplicated
        # Otherwise add first and last digit
        matches = [match.group() for match in re.finditer(r"\d", line)]
        if len(matches) == 1:
            return int(matches[0] + matches[0])
        else:
            return int(matches[0] + matches[-1])

    @staticmethod
    def replace_substring_with_digit(original_string, substring_to_replace, digit):
        """
        Part 2 of Day 1 needs to replace spelled out digits in each line with the actual digit.
        :param original_string: The input line with spelled out digits
        :param substring_to_replace: target digits to be replaced in the string
        :param digit:
        :return:
        """
        pattern = re.escape(substring_to_replace)
        result_string = re.sub(pattern, str(digit), original_string)
        return result_string

    def convert_line(self, line):
        final_line = line

        # First check for 'special' (overlapping) digits...
        for key, value in self.special_digits_mapping.items():
            final_line = self.replace_substring_with_digit(final_line, key, value)
        # ...and then replace all spelled out digits with actual digit
        for key, value in self.spelled_digit_mapping.items():
            final_line = self.replace_substring_with_digit(final_line, key, value)
        return final_line

    def run_part1(self):
        input_array = np.array([Day1.extract_cal_val(line) for line in self.input.lines])
        check_sum = input_array.sum()
        print(check_sum)
        return check_sum

    def run_part2(self):

        converted_lines = [self.convert_line(line) for line in self.input.lines]
        input_array = np.array([Day1.extract_cal_val(line) for line in converted_lines])
        check_sum = input_array.sum()
        print(check_sum)
        return check_sum


if __name__ == '__main__':

    Day1 = Day1()
    Day1.run_part1()
    Day1.run_part2()
