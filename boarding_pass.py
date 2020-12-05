class BoardingPass:
    # Create a boarding pass set and load in the contents of a file.
    def __init__(self, filename):
        self.filename = filename
        self.passes = {}           # Id -> String.

        with open(filename) as f:
            for line in f:
                # Record a boarding pass
                bp = line.strip()

                # Convert to a number and store in map
                id = self.to_num(bp)
                self.passes[id] = bp

    @staticmethod
    # Get ID number of a boarding pass string.
    # B and F in first seven places correspond to binary 1 and 0, respectively.
    # R and L in last three places correspond to binary 1 and 0 respectively
    def to_num(bp):
        n = 0
        for c in bp:
            # Shift the id one bit to the left
            n <<= 1
            if c in 'BR':
                # Insert a 1 bit.  (Otherwise a 0 is inserted implicitly)
                n += 1

        return n

    # Find the highest number boarding pass id.
    def find_max(self):
        found = 0
        for n in self.passes:
            if n > found:
                found = n

        return found

    # Find the missing boarding pass.
    # It's the one that's missing from the set but the ids one higher and lower are in the set.
    def find_missing(self):
        found = None
        for n in range(1024):
            if (n not in self.passes) & (n-1 in self.passes) & (n+1 in self.passes):
                found = n

        return found

