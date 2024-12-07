"""Day 2 module"""

from copy import deepcopy


class Day2:
    """Class for solving day 2 problem"""

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
        lines = self.file_reader.read_lines("day2/input.txt")

        for line in lines:
            original = line.split()
            original = [int(element) for element in original]

            unique = deepcopy(original)
            unique = len(set(unique)) == len(original)

            ascending = deepcopy(original)
            ascending.sort()
            is_ascending = ascending == original

            descending = deepcopy(original)
            descending.sort(reverse=True)
            is_descending = descending == original

            if unique and (is_ascending or is_descending):

                if self.determine_if_list_is_valid(original):
                    total += 1

        # Print success of value.
        self.ui.print_success(f"The total is: {total}")

    def solve_problem_2(self):
        """Solve problem 2"""

        total = 0
        # Get the lines of input
        lines = self.file_reader.read_lines("day2/input.txt")

        for line in lines:
            original = line.split()
            original = [int(element) for element in original]

            altered_is_valid = False

            for i in range(len(original)):

                altered = deepcopy(original)
                altered.pop(i)

                unique = deepcopy(altered)
                unique = len(set(unique)) == len(altered)

                ascending = deepcopy(altered)
                ascending.sort()
                is_ascending = ascending == altered

                descending = deepcopy(altered)
                descending.sort(reverse=True)
                is_descending = descending == altered

                if unique and (is_ascending or is_descending):

                    if self.determine_if_list_is_valid(altered):
                        altered_is_valid = True

            if altered_is_valid:
                total += 1

        # Print success of value.
        self.ui.print_success(f"The total is: {total}")

    def determine_if_list_is_valid(self, the_list):
        """Determine if the list is valid"""
        line_valid = True
        for i in range(len(the_list) - 1):
            diff = abs(the_list[i] - the_list[i + 1])
            if diff < 1 or diff > 3:
                line_valid = False
        return line_valid
