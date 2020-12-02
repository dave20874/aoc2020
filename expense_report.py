from itertools import combinations
from functools import reduce

# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3], 2)

class ExpenseReport:
    def __init__(self, filename):
        self.filename = filename
        self.items = []
        f = open(self.filename, "r")
        for line in f.readlines():
            item = int(line.strip())
            self.items.append(item)

    def part1(self):
        answer = None
        for comb in combinations(self.items, 2):
            s = sum(comb, 0)
            if s == 2020:
                answer = reduce((lambda x, y: x * y), comb)

        return answer

    def part2(self):
        answer = None
        for comb in combinations(self.items, 3):
            s = sum(comb, 0)
            if s == 2020:
                answer = reduce((lambda x, y: x * y), comb)

        return answer

