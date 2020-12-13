from math import gcd

class Schedule:
    def __init__(self, filename):
        self.filename = filename
        self.time = 0
        self.buses = []
        self.load()


    def load(self):
        with open(self.filename) as f:
            # Read time
            self.time = int(f.readline())
            # print(f"Time: {self.time}")

            # Read bus ids
            ids = f.readline().strip().split(',')
            # print(f"ids: {ids}")

            for id in ids:
                if id == 'x':
                    self.buses.append(None)
                else:
                    self.buses.append(int(id))

    def part1(self):
        best_time = None
        best_bus = None
        for bus in self.buses:
            if bus is not None:
                until_departure = (bus - self.time % bus) % bus
                if best_time is None:
                    best_time = until_departure
                    best_bus = bus
                elif best_time > until_departure:
                    best_time = until_departure
                    best_bus = bus

        # print(f"Best bus {best_bus} wait {best_time} minutes.")
        return best_time * best_bus

    def part2(self):
        # We start by constructing a list of (period, offset) values we need to satisfy.
        # Each one means that at time t, a bus with period <period> should arrive after <offset>
        # minutes.
        period_offset = []
        for index, bus in enumerate(self.buses):
            if bus is not None:
                period_offset.append((bus, index % bus))

        # We will step forward in time, checking to see if any of the constraints in period_offset
        # are met.  When one is met, we take it out of the period_offset list and increase time
        # step by a factor of this period so the constraint is preserved for all steps forward.

        t = 0     # Start search at t=0
        t_step = 1   # Time will advance in steps of lcm, initially this is 1.

        # The search will continue until all constraints satisfied.
        while len(period_offset) > 0:
            # new_period_offset = []
            for period, offset in period_offset:
                residue = t % period
                to_wait = (period-residue) % period
                if to_wait == offset:
                    # We've satisfied this bus, only increase time in multiples of it's period now
                    t_step *= period // gcd(t_step, period)
                    period_offset.remove((period, offset))

            if len(period_offset) > 0:
                # Advance time for next round
                t += t_step

        return t


if __name__ == '__main__':
    schedule = Schedule("data/day13_input.txt")
    print(f"solution: {schedule.part2()}")
