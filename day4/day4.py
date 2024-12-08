"""Day 4 module"""

import re
from copy import deepcopy


class Day4:
    """Class for solving day 4 problem"""

    def __init__(self, ui, file_reader):
        """Constructor"""
        self.ui = ui
        self.file_reader = file_reader

    def run(self):
        """Run method"""
        choice = self.ui.display_problem_menu_and_get_response()
        while choice != self.ui.MAX_PROBLEM_MENU_CHOICES:
            if choice == 1:
                # Do Problem 1
                self.solve_problem_1()
            elif choice == 2:
                # Do Problem 2
                self.solve_problem_2()

            choice = self.ui.display_problem_menu_and_get_response()

    def solve_problem_1(self):
        """Solve problem 1"""

        total = 0
        word_search = []
        # Get the lines of input
        lines = self.file_reader.read_lines("day4/input.txt")
        for line in lines:
            word_search.append(list(line))

        # Get the transposed version of the word search
        transposed = self.transpose_word_search(word_search)
        # Get the rotated version of the word search
        rotated = self.rotate_word_search_to_diagonal(word_search)
        # Get the rotated and transposed version of the word search
        rotated_reversed = self.reverse_word_search_rows(word_search)
        rotated_reversed = self.rotate_word_search_to_diagonal(rotated_reversed)

        # Regex pattern to find.
        pattern1 = r"XMAS"
        pattern2 = r"SAMX"

        for row in word_search:
            # print(row)
            string_row = "".join(row)

            results1 = re.findall(pattern1, string_row)
            total += len(results1)

            results2 = re.findall(pattern2, string_row)
            total += len(results2)

        for row in transposed:
            # print(row)
            string_row = "".join(row)

            results1 = re.findall(pattern1, string_row)
            total += len(results1)

            results2 = re.findall(pattern2, string_row)
            total += len(results2)

        # Goes from top right to bottom left of original.
        for row in rotated:
            # print(row)
            string_row = "".join(row)

            results1 = re.findall(pattern1, string_row)
            total += len(results1)

            results2 = re.findall(pattern2, string_row)
            total += len(results2)

        # Goes from top left to bottom right of original.
        for row in rotated_reversed:
            # print(row)
            string_row = "".join(row)

            results1 = re.findall(pattern1, string_row)
            total += len(results1)

            results2 = re.findall(pattern2, string_row)
            total += len(results2)

        # Print success of value.
        self.ui.print_success(f"The total is: {total}")
        raise ValueError("FOOBAR")

    def solve_problem_2(self):
        """Solve problem 2"""

        total = 0
        # Get the lines of input
        lines = self.file_reader.read_lines("day4/sample_input.txt")

        # Print success of value.
        self.ui.print_success(f"The total is: {total}")
        raise ValueError("FOOBAR")

    def transpose_word_search(self, word_search):
        """Transpose a word search"""
        width = len(word_search)
        length = len(word_search[0])
        # Init a transposed word search filled with the letter "e"
        transposed = [["e"] * width for i in range(length)]
        # Do the actual transpose
        for i in range(width):
            for j in range(length):
                transposed[j][i] = word_search[i][j]

        return transposed

    def rotate_word_search_to_diagonal(self, word_search):
        """Rotate word search to diagonal"""
        rotated = []
        for i, row in enumerate(word_search):
            for j, val in enumerate(row):
                # Ensure the result list is long enough
                while i + j >= len(rotated):
                    rotated.append([])

                rotated[i + j].append(val)

        return rotated

    def reverse_word_search_rows(self, word_search):
        """Reverse each row in the word search"""
        reversed_ws = []
        for row in word_search:
            new_row = deepcopy(row)
            new_row.reverse()
            reversed_ws.append(new_row)

        return reversed_ws
