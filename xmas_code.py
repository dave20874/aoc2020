class XmasCode:
    def __init__(self, filename, window_len=50):
        self.window_len = window_len
        self.data = []
        self.cursor = 0
        self.load(filename)

    def load(self, filename):
        # Load input into a list.  The file is simply one integer per line.
        self.data = []
        with open(filename) as f:
            for l in f:
                self.data.append(int(l))

        self.cursor = 0

    # Position the cursor beyond the preamble part.
    def scan_preamble(self):
        self.cursor += self.window_len

    # Check the value at cursor, is it a valid value?  Always advances cursor
    # return (Boolean, value) where boolean is true if it's valid.
    def read_one(self):
        value = self.data[self.cursor]
        window_base = self.cursor-self.window_len
        self.cursor += 1
        # Check all pairs of indices in the window to see if they produce a value that equals
        # the next value in the sequence.
        for n in range(self.window_len-1):
            for m in range(n+1, self.window_len, 1):
                if self.data[window_base+n] + self.data[window_base+m] == value:
                    # This value is valid since it equals the sum of a pair in the window.
                    return (True, value)

        # Didn't find a sum that worked
        return (False, value)


    def find_mismatch(self):
        self.scan_preamble()
        valid = True
        value = None
        # Use read_one in a loop until we find the invalid value.
        while valid:
            valid, value = self.read_one()
            # print(f"Searching: {valid}, {value}")

        return (valid, value)

    def find_weakness(self):
        valid, special = self.find_mismatch()

        # We're looking for contiguous numbers that sum to special
        # the range tail, head (inclusive) is walked through the list trying to
        # create a sum that equals the special value computed above.
        #
        # We start head, tail at zero and whenever the sum is too small, we move
        # the head (adding in a new element.)  When too large, we move tail, dropping
        # an old element.
        tail = 0
        head = 0
        sum = self.data[0]
        # print(f"Special value is {special}")
        while head < len(self.data):
            # print(f"Examining range {tail} - {head}, sum is {sum}")
            if sum < special:
                # grow from head
                # print(f"Sum {sum} too small, growing head to {head+1}")
                head += 1
                sum += self.data[head]
            elif sum > special:
                # print(f"Sum {sum} too great, moving tail to {tail+1}")
                # shrink from tail
                sum -= self.data[tail]
                tail += 1
            else:
                # Found the range
                # print(f"Found weakness range in {tail}-{head}")
                break

        # Now that we have the range tail to head, pick out the min and max values in that range
        # Then add them up as the solution to the puzzle.
        if sum == special:
            min_val = min(self.data[tail:head+1])
            max_val = max(self.data[tail:head+1])
            # print(f"min:{min_val} + max:{max_val} = {min_val+max_val}")
            return min_val+max_val

        # Well, we tried anyway.
        return None



