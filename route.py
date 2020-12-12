import re

# A tiny helper class to hold operations and distances loaded from input file.
class Op:
    def __init__(self, op, dist):
        self.op = op
        self.dist = dist

# Day 12: Rain Risk Solver
class Route:
    INSTRUCTION_RE = re.compile("([NSEWFRL])([+-]?[0-9]+)")

    def __init__(self, filename):
        self.filename = filename
        self.instructions = []    # Instructions loaded from input file (list of Op)
        self.x = 0                # ferry position and heading
        self.y = 0
        self.hdg = 0
        self.waypoint_dx = 10     # Waypoint position relative to ferry
        self.waypoint_dy = 1

        self.load(filename)       # Load the given input file

    # Resets ferry and waypoint position
    def reset(self):
        self.x = 0              # Initial ferry position, heading
        self.y = 0
        self.hdg = 0
        self.waypoint_dx = 10   # Initial waypoint location
        self.waypoint_dy = 1

    # Load an input file
    def load(self, filename):
        self.reset()
        with open(filename) as f:
            for l in f.readlines():
                # Using regular expression to pick out fields of input file.
                # group(1) is operation, group(2) is argument
                m = Route.INSTRUCTION_RE.match(l.strip())
                if m:
                    op = m.group(1)
                    dist = int(m.group(2))
                    self.instructions.append(Op(op, dist))

    # Move as prescribed in part 1.
    # Each move updates x, y, hdg components of self.
    def move(self, i):
        if i.op == 'N':
            self.y += i.dist
        elif i.op == 'E':
            self.x += i.dist
        elif i.op == 'S':
            self.y -= i.dist
        elif i.op == 'W':
            self.x -= i.dist
        elif i.op == 'R':
            self.hdg = (self.hdg + i.dist) % 360
        elif i.op == 'L':
            self.hdg = (self.hdg - i.dist) % 360
        elif i.op == 'F':
            if self.hdg == 0:
                self.x += i.dist
            elif self.hdg == 90:
                self.y -= i.dist
            elif self.hdg == 180:
                self.x -= i.dist
            elif self.hdg == 270:
                self.y += i.dist
            else:
                raise Exception("Unhandled heading.")
        else:
            raise Exception("Unhandled operation.")

    # Move as prescribed in part 2.
    # Each move updates waypoint position or ferry position
    def move2(self, i):
        if i.op == 'N':
            self.waypoint_dy += i.dist
        elif i.op == 'E':
            self.waypoint_dx += i.dist
        elif i.op == 'S':
            self.waypoint_dy -= i.dist
        elif i.op == 'W':
            self.waypoint_dx -= i.dist
        elif i.op == 'R':
            angle = i.dist
            while angle > 0:
                self.waypoint_dx, self.waypoint_dy = self.waypoint_dy, -self.waypoint_dx
                angle -= 90
        elif i.op == 'L':
            angle = i.dist
            while angle > 0:
                self.waypoint_dx, self.waypoint_dy = -self.waypoint_dy, +self.waypoint_dx
                angle -= 90
        elif i.op == 'F':
            self.x += i.dist * self.waypoint_dx
            self.y += i.dist * self.waypoint_dy
        else:
            raise Exception("Unhandled operation.")

        # print(f"{i.op} {i.dist} -> ({self.x}, {self.y}) waypoint: ({self.waypoint_dx}, {self.waypoint_dy})")

    # Solve part 1 by moving repeated (with move1()) and reporting the manhattan distance moved.
    def part1(self):
        # Start at (0, 0), facing East (heading 0)
        self.reset()
        for i in self.instructions:
            self.move(i)
            # print(f"x:{self.x}, y:{self.y}, hdg:{self.hdg}")

        return abs(self.x) + abs(self.y)

    # Solve part 2 by moving repeatedly (with move2()) and reporting the manhattan distance moved.
    def part2(self):
        # Start at (0, 0), waypoint at (10, 1)
        self.reset()
        for i in self.instructions:
            self.move2(i)
            # print(f"x:{self.x}, y:{self.y}, hdg:{self.hdg}")

        return abs(self.x) + abs(self.y)


