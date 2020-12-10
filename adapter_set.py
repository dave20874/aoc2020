class AdapterSet:
    def __init__(self, filename):
        self.adapters = []             # List will include all adapter values PLUS 0 and highest+3.
        self.ways_to = {0: 1}
        self.load(filename)

    def load(self, filename):
        self.ways_to = {0: 1}          # Reset the cache of ways to <jolts>

        self.adapters = [0,]           # Start with 0, representing the outlet

        # Process the input file
        with open(filename) as f:
            for line in f:
                self.adapters.append(int(line))

        # sort adapter list, then diffs become trivial to evaluate.
        self.adapters.sort()

        # Add in highest+3, representing the device.
        highest = self.adapters[-1]
        self.adapters.append(highest+3)

    def part1(self):
        # count jolt differences.  diffs[jolt] = count
        diffs = {}
        for n in range(len(self.adapters)-1):
            # Look at diff from this adapter to the next
            diff = self.adapters[n+1] - self.adapters[n]

            # Increment the count for this diff (and, btw, add it to the dict if not already there.)
            if diff not in diffs:
                diffs[diff] = 0
            diffs[diff] += 1

        # Solution to part 1 is product of 1-jolt diffs and 3-jolt diffs
        return diffs[1] * diffs[3]

    # Compute how many ways there are to adapt 0 to jolts
    # Uses recursion but caches answers to we don't have to evaluate the same answer repeatedly.
    def compute_ways(self, jolts):
        # Check cache first.
        if jolts not in self.ways_to:
            # Not in cache, We have to figure it out
            ways = 0
            for other in [jolts-1, jolts-2, jolts-3]:
                # If we have an adapter to this lower jolt, add in the ways to get there.
                if other in self.adapters:
                    ways += self.compute_ways(other)

            # cache this to save doing a lot of work later.
            self.ways_to[jolts] = ways

        # print(f"Ways to {jolts}: {self.ways_to[jolts]}")
        return self.ways_to[jolts]

    def part2(self):
        # Solution to part 2 is the number of ways we can adapt to the device voltage.
        highest = self.adapters[-1]

        return self.compute_ways(highest)


