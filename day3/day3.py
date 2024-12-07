"""Day 3 module"""

import re


class Day3:
    """Class for solving day 3 problem"""

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
        # Get the lines of input
        lines = self.file_reader.read_lines("day3/input.txt")

        pattern = r"mul\(\d{1,3},\d{1,3}\)"

        for line in lines:
            results = re.findall(pattern, line)

            num_only_pattern = r"\d*,\d*"
            for result in results:
                num_results = re.findall(num_only_pattern, result)
                num_results = num_results[0]
                numbers = num_results.split(",")
                number = int(numbers[0]) * int(numbers[1])
                total += number

        # Print success of value.
        self.ui.print_success(f"The total is: {total}")

    def solve_problem_2(self):
        """Solve problem 2"""

        total = 0
        # Get the lines of input
        lines = self.file_reader.read_lines("day3/input.txt")

        pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

        do_work = True
        for line in lines:
            results = re.findall(pattern, line)

            num_only_pattern = r"\d*,\d*"
            for result in results:
                if result == "do()":
                    do_work = True
                elif result == "don't()":
                    do_work = False
                else:
                    if do_work:
                        num_results = re.findall(num_only_pattern, result)
                        num_results = num_results[0]
                        numbers = num_results.split(",")
                        number = int(numbers[0]) * int(numbers[1])
                        total += number

        # Print success of value.
        self.ui.print_success(f"The total is: {total}")
