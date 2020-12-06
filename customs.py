import itertools
import re

# Group represents a group of passengers travelling together and their responses
# to the questionaire.
class Group:
    def __init__(self):
        self.yeses = {}       # Map: question -> True for each question answered yes by someone
        self.responses = []   # Individual responses stored for part 2

    # Update the group with one travelers response
    def add_response(self, response):
        self.responses.append(response)
        for c in response:
            self.yeses[c] = True

    # Return the number of questions answered yes by at least one person
    def num_one_yes(self):
        return len(self.yeses)

    # return the number of questions answered yes by all people in the group
    def num_all_yes(self):
        n = 0
        for c in self.yeses:
            all = True
            for response in self.responses:
                if c not in response:
                    all = False
            if all:
                n += 1
        return n

# The overall problem representation.
class Customs:
    def __init__(self, filename):
        self.filename = filename
        self.groups = []
        self.load()

    def reset(self):
        self.groups = []

    # Load the input file, creating groups and adding data to them as we go
    def load(self):
        self.reset()
        group = None
        with open(self.filename) as f:
            for line in f:
                if line.strip() == "":
                    # Blank line marks end of group
                    self.groups.append(group)
                    group = None
                else:
                    if group is None:
                        group = Group()
                    group.add_response(line.strip())

        # Don't forget the last group
        if group is not None:
            self.groups.append(group)

    def part1(self):
        # Sum over groups the number of questions one person said yes to.
        return sum([x.num_one_yes() for x in self.groups])

    def part2(self):
        # Sum over groups the number of questions all persons said yes to.
        return sum([x.num_all_yes() for x in self.groups])
