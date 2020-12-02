from expense_report import ExpenseReport
from password_db import PasswordDb

class AocDay:
    def __init__(self, day_num):
        self.day_num = day_num

    def part1(self):
        return None

    def part2(self):
        return None

# ------------------------------------------------
class Day1(AocDay):
    def __init__(self):
        super().__init__(1)
        self.exp_rep = ExpenseReport("data/day1_input.txt")

    def part1(self):
        return self.exp_rep.part1()

    def part2(self):
        return self.exp_rep.part2()

# ------------------------------------------------
class Day2(AocDay):
    def __init__(self):
        super().__init__(2)
        self.passwords = PasswordDb()
        self.passwords.load_file("data/day2_input.txt")

    def part1(self):
        return self.passwords.num_valid()

    def part2(self):
        return self.passwords.num_valid2()

# ------------------------------------------------
class Day3(AocDay):
    def __init__(self):
        super().__init__(3)

# ------------------------------------------------
class Day4(AocDay):
    def __init__(self):
        super().__init__(4)

# ------------------------------------------------
class Day5(AocDay):
    def __init__(self):
        super().__init__(5)

# ------------------------------------------------
class Day6(AocDay):
    def __init__(self):
        super().__init__(6)

# ------------------------------------------------
class Day7(AocDay):
    def __init__(self):
        super().__init__(7)

# ------------------------------------------------
class Day8(AocDay):
    def __init__(self):
        super().__init__(8)

# ------------------------------------------------
class Day9(AocDay):
    def __init__(self):
        super().__init__(9)

# ------------------------------------------------
class Day10(AocDay):
    def __init__(self):
        super().__init__(10)

# ------------------------------------------------
class Day11(AocDay):
    def __init__(self):
        super().__init__(11)

# ------------------------------------------------
class Day12(AocDay):
    def __init__(self):
        super().__init__(12)

# ------------------------------------------------
class Day13(AocDay):
    def __init__(self):
        super().__init__(13)


# ------------------------------------------------
class Day14(AocDay):
    def __init__(self):
        super().__init__(14)


# ------------------------------------------------
class Day15(AocDay):
    def __init__(self):
        super().__init__(15)


# ------------------------------------------------
class Day16(AocDay):
    def __init__(self):
        super().__init__(16)


# ------------------------------------------------
class Day17(AocDay):
    def __init__(self):
        super().__init__(17)


# ------------------------------------------------
class Day18(AocDay):
    def __init__(self):
        super().__init__(18)


# ------------------------------------------------
class Day19(AocDay):
    def __init__(self):
        super().__init__(19)


# ------------------------------------------------
class Day20(AocDay):
    def __init__(self):
        super().__init__(20)


# ------------------------------------------------
class Day21(AocDay):
    def __init__(self):
        super().__init__(21)


# ------------------------------------------------
class Day22(AocDay):
    def __init__(self):
        super().__init__(22)


# ------------------------------------------------
class Day23(AocDay):
    def __init__(self):
        super().__init__(23)


# ------------------------------------------------
class Day24(AocDay):
    def __init__(self):
        super().__init__(24)


# ------------------------------------------------
class Day25(AocDay):
    def __init__(self):
        super().__init__(25)


# ------------------------------------------------


if __name__ == '__main__':
    days = (Day1(), Day2(), Day3(), Day4(), Day5(), Day6(), Day7(), Day8(), Day9(), Day10(),
            Day11(), Day12(), Day13(), Day14(), Day15(), Day16(), Day17(), Day18(), Day19(), Day20(),
            Day21(), Day22(), Day23(), Day24(), Day25())

    for (index, day) in enumerate(days):
        part1 = day.part1()
        if part1 is not None:
            print(f"Day {day.day_num}, Part 1: {part1}")

        part2 = day.part2()
        if part2 is not None:
            print(f"Day {day.day_num}, Part 2: {part2}")
