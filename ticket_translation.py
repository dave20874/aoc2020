import re

class Field:
    def __init__(self, name, min1, max1, min2, max2):
        self.name = name
        self.min1 = min1
        self.max1 = max1
        self.min2 = min2
        self.max2 = max2
        self.index = 0

    def is_ok(self, value):
        return (((value >= self.min1) & (value <= self.max1)) |
                (value >= self.min2) & (value <= self.max2))

    def set_col(self, index):
        self.index = index


class TicketInfo:
    YOUR_TICKET_RE = re.compile("your ticket:")
    NEARBY_RE = re.compile("nearby tickets")

    # Groups:
    # 1 - field name; 2,3 - range1 min, max; 4,5 - range 2 min, max
    FIELD_RE = re.compile("(.*): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)")

    def __init__(self, filename):
        self.filename = filename
        self.fields = {}
        self.mine = []
        self.nearby = []
        self.valid_tickets = []
        self.load()

    def load_field(self, line):
        m = TicketInfo.FIELD_RE.match(line)
        if m:
            name = m.group(1)
            min1 = int(m.group(2))
            max1 = int(m.group(3))
            min2 = int(m.group(4))
            max2 = int(m.group(5))
            self.fields[name] = Field(name, min1, max1, min2, max2)

    def load_mine(self, line):
        vals = line.split(',')
        if len(vals) == 0:
            # Ignore this line
            pass
        elif len(vals) != len(self.fields):
            # print(f"Loading mine: {line}")
            # raise Exception(f"Wrong number of fields for my ticket: {len(vals)} vs {len(self.fields)}")
            pass
        else:
            self.mine = [int(val) for val in vals]

    def load_nearby(self, line):
        vals = line.split(',')
        if len(vals) == 0:
            # Ignore this line
            pass
        elif len(vals) != len(self.fields):
            # raise Exception("Wrong number of fields for nearby ticket")
            pass
        else:
            vals = [int(val) for val in vals]
            self.nearby.append(vals)

    def load(self):
        self.nearby = []
        self.valid_tickets = []
        self.mine = []
        self.fields = {}

        phase = "fields"
        with open(self.filename) as f:
            for line in f.readlines():
                if TicketInfo.YOUR_TICKET_RE.match(line):
                    # Go to your ticket phase of input
                    phase = "your ticket"
                elif TicketInfo.NEARBY_RE.match(line):
                    # Go to nearby tickets phase
                    phase = "nearby"
                else:
                    # Process line according to phase
                    if phase == "fields":
                        self.load_field(line)
                    elif phase == "your ticket":
                        self.load_mine(line)
                    elif phase == "nearby":
                        self.load_nearby(line)
                    else:
                        raise Exception("File processor off the rails.")

    # For part 1, a ticket is invalid if it contains a value that can't pass ANY field
    def scan_err_rate(self):
        err_rate = 0
        self.valid_tickets = []

        for ticket in self.nearby:
            bad_ticket = False
            for value in ticket:
                passes_some = False
                for name in self.fields:
                    if self.fields[name].is_ok(value):
                        passes_some = True

                if not passes_some:
                    # This value is invalid in EVERY field, add it to err_rate
                    err_rate += value
                    bad_ticket = True

            if not bad_ticket:
                self.valid_tickets.append(ticket)

        return err_rate

    def id_fields(self):
        # Start by checking every field rule against every column, to determine which
        # columns could possibly be that field
        possible_cols = {}  # map field name -> column index
        for field_name in self.fields:
            possible_cols[field_name] = []
            field = self.fields[field_name]
            for index in range(len(self.valid_tickets[0])):
                # Checking column <index> against <field>
                all_valid = True
                for ticket in self.valid_tickets:
                    if not field.is_ok(ticket[index]):
                        all_valid = False
                        break

                if all_valid:
                    possible_cols[field_name].append(index)

        # Next, identify which column is actually which field
        assigned_col = {}  # Name -> column
        done = False
        while not done:
            done = True  # Unless we see a field that's still ambiguous.
            for name in possible_cols:
                if len(possible_cols[name]) == 1:
                    # Assign this col to this name
                    col = possible_cols[name][0]
                    assigned_col[name] = col
                    self.fields[name].set_col(col)
                    # print(f"{name} must be {col}")

                    # Remove it from all others
                    for other_name in possible_cols:
                        if other_name != name:
                            if col in possible_cols[other_name]:
                                possible_cols[other_name].remove(col)
                else:
                    done = False

    def part2(self):
        # First discard the invalid tickets
        self.scan_err_rate()

        # Second, figure out field assignments
        self.id_fields()

        # Third, retrieve "departure" fields
        prod = 1
        for field_name in self.fields:
            value = self.mine[self.fields[field_name].index]
            # print(f"{field_name} {value}")
            if "departure" in field_name:
                prod *= value

        return prod

if __name__ == "__main__":
    ti = TicketInfo("data/day16_input.txt")
    print(f"Part 1: {ti.scan_err_rate()}")
    print(f"Part 2: {ti.part2()}")
