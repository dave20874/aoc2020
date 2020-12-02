# Reads daily solutions from a file for use in unit testing.
# (Input file should not be git.)

# from itertools import sequence

# Reads a file with Advent of Code solutions.
# Each line contains two numbers separated by whitespace.
# The first line contains test values, the others represent solutions to AoC days starting with 1.

class SolutionSet:
    def __init__(self):
        self.solutions = {}  # Map: day -> (part1, part2)
        f = open("data/solutions.txt", "r")
        for (n, line) in enumerate(f.readlines()):
            parts = line.split(" ")
            self.solutions[n] = ( int(parts[0].strip()), int(parts[1].strip()), )

    # Get solution for day, part.  (Day is 1-25, Part is 1 or 2)
    def get_solution(self, day, part):
        # Return what's in the solution set for this day, this part.
        if day in self.solutions:
            if part-1 < len(self.solutions[day]):
                return self.solutions[day][part-1]

        # We don't have this solution.
        return None

    def get_num_solutions(self):
        return len(self.solutions)-1    # The test values in entry 0 don't count.
