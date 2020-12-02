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

    """
    def part2(self):
        answer = None
        for n in range(len(self.items)-2):
            for m in range(n+1, len(self.items)-1):
                for o in range(m+1, len(self.items)):
                    a = self.items[n]
                    b = self.items[m]
                    c = self.items[o]
                    sum = a + b + c
                    if sum == 2020:

                        prod = a * b * c
                        # print(f"Found {a} + {b} + {c} = {sum}")
                        # print(f"      {a} * {b} * {c} = {prod}")
                        answer = prod

        return answer
    """
