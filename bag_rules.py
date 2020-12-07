import re

class BagRules:
    RULE_RE = re.compile("([a-z]+ [a-z]+) bags contain (.*)")
    CONTAINED_RE = re.compile("([0-9]+) ([a-z]+ [a-z]+) bag[s]?")

    def __init__(self, filename):
        self.filename = filename

        # two-way maps for contains and contained-by relationships
        self.contains = {}   # map colorA -> list of (count, colorB)
        self.contained_by = {}  # map colorB -> colorA

        self.load(self.filename)

    def reset(self):
        # two-way maps for contains and contained-by relationships
        self.contains = {}   # map colorA -> list of (colorB, count)
        self.contained_by = {}  # map colorB -> colorA

    def load(self, filename):
        self.reset()
        with open(filename) as f:
            for line in f:
                # Process one line
                m = BagRules.RULE_RE.match(line)
                if m:
                    colorA = m.group(1)              # Containing bag color, colorA
                    contained_str = m.group(2)       # All the stuff it contains

                    # Split the contained_str into a list of (count, colorB) for contained bags.
                    contained_list = BagRules.CONTAINED_RE.findall(contained_str)
                    contained = []

                    # register the new colorA in contained_by if not there already
                    if not colorA in self.contained_by:
                        self.contained_by[colorA] = []

                    # Update contained and contained_by sets with each additional contained item
                    for count, colorB in contained_list:
                        # print(f"  {int(count)} {colorB}")
                        contained.append( (int(count), colorB) )
                        if not colorB in self.contained_by:
                            self.contained_by[colorB] = []
                        self.contained_by[colorB].append(colorA)

                    self.contains[colorA] = contained

    def num_rules(self):
        return len(self.contains)

    # Get the number of outer bag colors that contain this one.
    def num_outer(self, color):
        # With outer, we build a list of all the containing colors (plus the color itself)
        outer = []

        # to_add is a list of containing colors we need to include
        to_add = [color,]

        # Search for including colors until to_add is exhausted.
        while to_add:
            new_color = to_add.pop(0)
            if new_color not in outer:
                outer.append(new_color)
            for next_color in self.contained_by[new_color]:
                if next_color not in to_add:
                    to_add.append(next_color)

        # My outer set contains the original color so don't count that.
        return len(outer)-1

    def contained_in(self, color, level=0):
        n = 0
        for count, colorB in self.contains[color]:
            n += count + count * self.contained_in(colorB, level=level+1)

        return n




