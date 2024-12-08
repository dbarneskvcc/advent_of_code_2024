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

    def solve_problem_2(self):
        """Solve problem 2"""

        total = 0
        word_search = []
        a_locations = []

        # Get the lines of input and create word search
        lines = self.file_reader.read_lines("day4/input.txt")
        for line in lines:
            word_search.append(list(line))

        # Find the location of all "A"s
        for row_idx, row in enumerate(word_search):
            for col_idx, val in enumerate(row):
                if val == "A":
                    a_locations.append((row_idx, col_idx))

        # print(a_locations)

        # For each coord of "A", check to see if it is part of a cross.
        for coord in a_locations:
            if self.check_for_cross(coord, word_search):
                total += 1

        # Print success of value.
        self.ui.print_success(f"The total is: {total}")

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

    def check_for_cross(self, coord, word_search):
        """ "Check to see if surrounding area is a cross of MAS"""
        return_value = False
        y = coord[0]
        x = coord[1]

        # If the "A" is on the outside of the word search, it can not be part of "MAS"
        if y <= 0 or x <= 0 or y >= len(word_search) - 1 or x >= len(word_search) - 1:
            return False

        # M M
        #  A
        # S S
        if (
            # Top left
            word_search[y - 1][x - 1] == "M"
            # Top right
            and word_search[y - 1][x + 1] == "M"
            # Bottom left
            and word_search[y + 1][x - 1] == "S"
            # Bottom right
            and word_search[y + 1][x + 1] == "S"
        ):
            return_value = True
        # S M
        #  A
        # S M
        elif (
            # Top left
            word_search[y - 1][x - 1] == "S"
            # Top right
            and word_search[y - 1][x + 1] == "M"
            # Bottom left
            and word_search[y + 1][x - 1] == "S"
            # Bottom right
            and word_search[y + 1][x + 1] == "M"
        ):
            return_value = True
        # M S
        #  A
        # M S
        elif (
            # Top left
            word_search[y - 1][x - 1] == "M"
            # Top right
            and word_search[y - 1][x + 1] == "S"
            # Bottom left
            and word_search[y + 1][x - 1] == "M"
            # Bottom right
            and word_search[y + 1][x + 1] == "S"
        ):
            return_value = True
        # S S
        #  A
        # M M
        elif (
            # Top left
            word_search[y - 1][x - 1] == "S"
            # Top right
            and word_search[y - 1][x + 1] == "S"
            # Bottom left
            and word_search[y + 1][x - 1] == "M"
            # Bottom right
            and word_search[y + 1][x + 1] == "M"
        ):
            return_value = True

        return return_value
