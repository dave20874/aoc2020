# Advent of Code 2020
# The annual challenge, by Eric Wastl, can be found at https://adventofcode.com/2020
#
# This project, by David Wheeler, is an attempted solution in Python with unit tests.

from functools import reduce

# Support classes developed along the way
from expense_report import ExpenseReport     # For Day 1
from password_db import PasswordDb           # For Day 2
from forest import Forest                    # For Day 3
from passports import Passports              # For Day 4
from boarding_pass import BoardingPass       # For Day 5
from customs import Customs                  # For Day 6
from bag_rules import BagRules               # For Day 7
from computer import Computer                # For Day 8
from xmas_code import XmasCode               # For Day 9
from adapter_set import AdapterSet           # For Day 10
from seating import Seating                  # For Day 11
from route import Route                      # For Day 12
from shuttle_search import Schedule          # For Day 13
from docking_data import DockingData         # For Day 14
from rambunctious_recitation import Recitation  # For Day 15
from ticket_translation import TicketInfo    # For Day 16
from conway_cubes import ConwayCubes         # Day 17
from operator_order import OperatorOrder     # Day 18
from monster_messages import MonsterMessages # Day 19


# Base class for an Advent of Code daily class.
# A separate class supports each day with methods part1() and part2()
# that return the daily solutions for that day.
#
# The base class records the day number and has part1() and part2() simply
# return None to indicate an unimplemented day.
# (The main function in this file, doesn't show results for unimplemented days.)
class AocDay:
    def __init__(self, day_num):
        self.day_num = day_num

    def part1(self):
        return None

    def part2(self):
        return None

# ------------------------------------------------
# Day 1 : Report Repair

class Day1(AocDay):
    def __init__(self):
        super().__init__(1)
        # Load the daily input into an expense report
        self.exp_rep = ExpenseReport("data/day1_input.txt")

    def part1(self):
        # Expense Report knows how to compute part 1 solution
        return self.exp_rep.part1()

    def part2(self):
        # Expense Report knows how to compute part 2 solution
        return self.exp_rep.part2()

# ------------------------------------------------
# Day 2 : Password Philosophy

class Day2(AocDay):
    def __init__(self):
        super().__init__(2)
        # Load the daily input into a password database
        self.passwords = PasswordDb()
        self.passwords.load_file("data/day2_input.txt")

    def part1(self):
        # Answer is number of records passing validity check 1.
        return self.passwords.num_valid()

    def part2(self):
        # Answer is number of records passing validity check 2
        return self.passwords.num_valid2()

# ------------------------------------------------
class Day3(AocDay):
    def __init__(self):
        super().__init__(3)
        self.forest = Forest("data/day3_input.txt")

    def part1(self):
        return self.forest.get_num_trees(3, 1)

    def part2(self):
        slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

        # See how many trees we hit on each slope
        trees_hit = map((lambda slope: self.forest.get_num_trees(slope[0], slope[1])), slopes)

        # Multiply those numbers together
        prod = reduce((lambda x, y: x * y), trees_hit)

        # That's the answer
        return prod

# ------------------------------------------------
class Day4(AocDay):
    def __init__(self):
        super().__init__(4)
        self.passports = Passports("data/day4_input.txt")

    def part1(self):
        return Passports("data/day4_input.txt").validate()

    def part2(self):
        return Passports("data/day4_input.txt").validate(check_fields=True)

# ------------------------------------------------
class Day5(AocDay):
    def __init__(self):
        super().__init__(5)

    def part1(self):
        passes = BoardingPass("data/day5_input.txt")
        return passes.find_max()

    def part2(self):
        passes = BoardingPass("data/day5_input.txt")
        return passes.find_missing()

# ------------------------------------------------
class Day6(AocDay):
    def __init__(self):
        super().__init__(6)

    def part1(self):
        dummy = Customs("data/day6_input.txt")
        return dummy.part1()

    def part2(self):
        dummy = Customs("data/day6_input.txt")
        return dummy.part2()

# ------------------------------------------------
class Day7(AocDay):
    def __init__(self):
        super().__init__(7)

    def part1(self):
        rules = BagRules("data/day7_input.txt")
        return rules.num_outer("shiny gold")

    def part2(self):
        rules = BagRules("data/day7_input.txt")
        return rules.contained_in("shiny gold")

# ------------------------------------------------
class Day8(AocDay):
    PROGRAM = "data/day8_input.txt"

    def __init__(self):
        super().__init__(8)

    def part1(self):
        comp = Computer(Day8.PROGRAM)
        comp.reset()
        halted = comp.runToRepeat()
        return comp.acc

    def part2(self):
        comp = Computer(Day8.PROGRAM)
        comp.fixLoop()

        return comp.acc


# ------------------------------------------------
class Day9(AocDay):
    def __init__(self):
        super().__init__(9)

    def part1(self):
        code = XmasCode("data/day9_input.txt", 50)
        code.scan_preamble()
        check, value = code.find_mismatch()
        assert check == False
        return value

    def part2(self):
        code = XmasCode("data/day9_input.txt", 50)
        value = code.find_weakness()
        return value

# ------------------------------------------------
class Day10(AocDay):
    def __init__(self):
        super().__init__(10)
        self.adapters = AdapterSet("data/day10_input.txt")

    def part1(self):
        return self.adapters.part1();

    def part2(self):
        return self.adapters.part2();

# ------------------------------------------------
class Day11(AocDay):
    def __init__(self):
        super().__init__(11)
        self.seating = Seating("data/day11_input.txt")

    def part1(self):
        return self.seating.part1()

    def part2(self):
        return self.seating.part2()

# ------------------------------------------------
class Day12(AocDay):
    def __init__(self):
        super().__init__(12)

    def part1(self):
        route = Route("data/day12_input.txt")
        return route.part1()

    def part2(self):
        route = Route("data/day12_input.txt")
        return route.part2()

# ------------------------------------------------
class Day13(AocDay):
    def __init__(self):
        super().__init__(13)

    def part1(self):
        schedule = Schedule("data/day13_input.txt")
        return schedule.part1()

    def part2(self):
        schedule = Schedule("data/day13_input.txt")
        return schedule.part2()

# ------------------------------------------------
class Day14(AocDay):
    def __init__(self):
        super().__init__(14)

    def part1(self):
        dd = DockingData()
        dd.load("data/day14_input.txt")
        return dd.get_sum()

    def part2(self):
        dd = DockingData()
        dd.load2("data/day14_input.txt")
        return dd.get_sum()

# ------------------------------------------------
class Day15(AocDay):
    def __init__(self):
        super().__init__(15)

    def part1(self):
        rec = Recitation("data/day15_input.txt")
        rec.start()
        return rec.play_to(2020)

    def part2(self):
        rec = Recitation("data/day15_input.txt")
        rec.start()
        return rec.play_to(30000000)

# ------------------------------------------------
class Day16(AocDay):
    def __init__(self):
        super().__init__(16)

    def part1(self):
        ti = TicketInfo("data/day16_input.txt")
        return ti.scan_err_rate()

    def part2(self):
        ti = TicketInfo("data/day16_input.txt")
        return ti.part2()

# ------------------------------------------------
class Day17(AocDay):
    def __init__(self):
        super().__init__(17)

    def part1(self):
        cc = ConwayCubes("data/day17_input.txt", 3)
        for n in range(6):
            cc.step()
        return cc.active_cubes();

    def part2(self):
        cc = ConwayCubes("data/day17_input.txt", 4)
        for n in range(6):
            cc.step()
        return cc.active_cubes();


# ------------------------------------------------
class Day18(AocDay):
    def __init__(self):
        super().__init__(18)

    def part1(self):
        oo = OperatorOrder("data/day18_input.txt")
        return oo.part1()

    def part2(self):
        oo = OperatorOrder("data/day18_input.txt")
        return oo.part2()

# ------------------------------------------------
class Day19(AocDay):
    def __init__(self):
        super().__init__(19)

    def part1(self):
        mm = MonsterMessages("data/day19_input.txt")
        return mm.num_match()

    def part2(self):
        mm = MonsterMessages("data/day19_input.txt")
        return mm.part2()

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
    # A tuple of daily puzzle solvers
    days = (Day1(), Day2(), Day3(), Day4(), Day5(), Day6(), Day7(), Day8(), Day9(), Day10(),
            Day11(), Day12(), Day13(), Day14(), Day15(), Day16(), Day17(), Day18(), Day19(), Day20(),
            Day21(), Day22(), Day23(), Day24(), Day25())

    # Solve all the days and print solutions.
    # (Unimplemented days return None as the solution and we don't print those.)
    for day in days:
        # Solve part 1
        part1 = day.part1()
        if part1 is not None:
            print(f"Day {day.day_num}, Part 1: {part1}")

        # Solve part 2
        part2 = day.part2()
        if part2 is not None:
            print(f"Day {day.day_num}, Part 2: {part2}")
