import re

class DockingData:
    # Regular expressions for parsing input file
    MASK_RE = re.compile("mask = ([01X]+)")                # group(1): mask string
    WRITE_RE = re.compile("mem\\[([0-9]+)\\] = ([0-9]+)")  # group(1): addr, group(2): data

    def __init__(self):
        self.mem = {}
        self.and_mask = 0
        self.or_mask = 0

    def reset(self):
        self.mem = {}
        self.and_mask = 0
        self.or_mask = 0

    # Based on mask string, sets a pair of numerical masks: and_mask and or_mask that
    # will force data bits to 0 or 1 when applied.
    def set_mask(self, mask_str):
        and_mask = 0
        or_mask = 0
        for c in mask_str:
            if c == '0':
                # Both or_mask and and_mask get a zero
                and_mask <<= 1
                or_mask <<= 1
            elif c == '1':
                # Both or_mask and and_mask get a one
                and_mask <<= 1
                and_mask |= 1
                or_mask <<= 1
                or_mask |= 1
            elif c == 'X':
                # or_mask gets zero, and_mask gets 1
                and_mask <<= 1
                and_mask |= 1
                or_mask <<= 1
            else:
                raise Exception("Invalid mask character.")

        self.or_mask = or_mask
        self.and_mask = and_mask

    # Read the input file, applying the data masking rules per part 1 of the challenge.
    def load(self, filename):
        self.reset()

        with open(filename) as f:
            for l in f.readlines():
                # print(f"Processing {l}")
                m = DockingData.MASK_RE.match(l)
                if m:
                    # Update mask
                    self.set_mask(m.group(1))
                    # print(f"Updated mask: {self.or_mask:09x}, {self.and_mask:09x}")

                m = DockingData.WRITE_RE.match(l)
                if m:
                    # Perform write operation
                    addr = int(m.group(1))
                    data = int(m.group(2))
                    self.mem[addr] = (data & self.and_mask) | self.or_mask
                    # print(f"Updated mem[{addr}] = {self.mem[addr]}")

    # Generate a list of addresses that correspond to base_addr under the part 2
    # address masking rules.
    def gen_addr(self, base_addr):
        out_addrs = [base_addr,]        # We build up the address set, starting with just the base addr itself.

        # Apply address masking rules one bit position at a time.
        for position in range(36):
            bit_mask = 1 << position
            if ((self.or_mask & bit_mask) & (self.and_mask & bit_mask)) != 0:
                # mask is '1', set this bit position to one in all addresses
                for n in range(len(out_addrs)):
                    out_addrs[n] |= bit_mask
            elif ((self.or_mask & bit_mask) == 0) & ((self.and_mask & bit_mask) == bit_mask):
                # mask is 'X', generate addresses with both 0 and 1 in this position
                # For every addr currently in out_addrs, create two.  One with 0 in this bit
                # position, the other with 1.
                doubled_addrs = []
                for n in range(len(out_addrs)):
                    doubled_addrs.append(out_addrs[n] | bit_mask)
                    doubled_addrs.append(out_addrs[n] & ~bit_mask)

                # Adopt the new doubled set of addresses as the result going forward.
                out_addrs = doubled_addrs

        return out_addrs

    # Load the input file, applying address masking rules per part 2 of the challenge.
    def load2(self, filename):
        self.reset()

        with open(filename) as f:
            for l in f.readlines():
                m = DockingData.MASK_RE.match(l)
                if m:
                    # Update mask
                    self.set_mask(m.group(1))

                m = DockingData.WRITE_RE.match(l)
                if m:
                    # Perform write operation
                    data = int(m.group(2))
                    base_addr = int(m.group(1))
                    for addr in self.gen_addr(base_addr):
                        self.mem[addr] = data

    def get_sum(self):
        return sum([self.mem[x] for x in self.mem])

if __name__ == '__main__':
    dd = DockingData()
    dd.load2("data/day14_example2.txt")
    print(f"Part 2, Example 2: {dd.get_sum()}")

