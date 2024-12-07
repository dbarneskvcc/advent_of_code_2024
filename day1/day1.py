"""Day 1 module"""


class Day1:
    """Class for solving day 1 problem"""

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

        # Accumulator the total of concatenated numbers.
        total = 0
        # Get the lines of input
        lines = self.file_reader.read_lines("day1/input.txt")
        # Left list
        left = []
        # Right list
        right = []
        # For each line start processing line
        for line in lines:
            # Split line by space
            parts = line.split()
            left.append(parts[0])
            right.append(parts[1])

        # Sort left and right
        left.sort()
        right.sort()

        total = 0
        for i in range(len(left)):
            diff = abs(int(left[i]) - int(right[i]))
            total += diff

        # Print success of value.
        self.ui.print_success(f"The total is: {total}")

    # def solve_problem_2(self):
    #     """Solve problem 2 naive with a Big O of O(N^2)"""

    #     # Accumulator the total of concatenated numbers.
    #     total = 0
    #     # Get the lines of input
    #     lines = self.file_reader.read_lines("day1/input.txt")
    #     # Left list
    #     left = []
    #     # Right list
    #     right = []
    #     # For each line start processing line
    #     for line in lines:
    #         # Split line by space
    #         parts = line.split()
    #         left.append(int(parts[0]))
    #         right.append(int(parts[1]))

    #     total = 0

    #     for l_element in left:
    #         counter = 0
    #         for r_element in right:
    #             if l_element == r_element:
    #                 counter +=1
    #         similarity = counter * l_element
    #         total += similarity

    #     # Print success of value.
    #     self.ui.print_success(f"The total is: {total}")

    def solve_problem_2(self):
        """Solve problem 2 with Big O of O(N)"""

        # Accumulator the total of concatenated numbers.
        total = 0
        # Get the lines of input
        lines = self.file_reader.read_lines("day1/input.txt")
        # Left list
        left = []
        # Right list
        right = []
        # For each line start processing line
        for line in lines:
            # Split line by space
            parts = line.split()
            left.append(int(parts[0]))
            right.append(int(parts[1]))

        total = 0

        right_dict = {}
        for element in right:
            if element not in right_dict:
                right_dict[element] = 1
            else:
                right_dict[element] += 1

        for l_element in left:
            counter = right_dict.get(l_element, 0)
            similarity = counter * l_element
            total += similarity

        # Print success of value.
        self.ui.print_success(f"The total is: {total}")
