import itertools

class ConwayCubes:
    def __init__(self, filename, dims):
        self.filename = filename
        self.dims = dims
        self.occupied = {}  # (x, y, z) -> True
        self.steps = 0
        self.initial = {}   # (x, y, z) -> True
        self.neighbor_cache = {}

        self.load()

    def reset(self):
        self.neighbor_cache = {}
        self.occupied = {}
        for coord2 in self.initial:
            coordN = [0,]*self.dims
            coordN[0] = coord2[0]
            coordN[1] = coord2[1]
            self.occupied[tuple(coordN)] = True

        self.steps = 0

    def load(self):
        self.initial = {}

        with open(self.filename) as f:
            for y, line in enumerate(f.readlines()):
                for x, c in enumerate(line.strip()):
                    if c == '#':
                        self.initial[(x, y)] = True

        # Reset to initial state
        self.reset()

    def neighbors(self, coord):
        if coord in self.neighbor_cache:
            return self.neighbor_cache[coord]

        zero = (0,)*self.dims
        retval = []
        for offset in itertools.product([-1, 0, 1], repeat=self.dims):
            if offset == zero:
                # A coord is not a neighbor of itself
                continue
            else:
                new_coord = [0]*self.dims
                for d in range(self.dims):
                    new_coord[d] = coord[d] + offset[d]
                retval.append(tuple(new_coord))

        self.neighbor_cache[coord] = tuple(retval)

        return tuple(retval)

    def step(self):
        # print(f"Stepping")
        # Collect all the coordinates to evaluate
        boundary = {}
        for coord in self.occupied:
            boundary[coord] = True
            for n in self.neighbors(coord):
                # print(f"Added {n} to boundary.")
                boundary[n] = True

        next_gen = {}
        for coord in boundary:
            count = 0
            for other in self.neighbors(coord):
                # print(f"  Testing if {other} in {self.occupied}")
                if other in self.occupied:
                    count += 1
            # print(f"Position {coord} has {count} neighbors.")

            if count == 3:
                # Come to life
                next_gen[coord] = True
            elif count == 2:
                # Stay alive if already alive
                if coord in self.occupied:
                    next_gen[coord] = True

        # replace old gen with new gen
        self.occupied = next_gen
        self.steps += 1

    def active_cubes(self):
        return len(self.occupied)

if __name__ == '__main__':
    cc = ConwayCubes("data/day17_input.txt", 3)
    for n in range(6):
        cc.step()
    print(f"Part 1: {cc.active_cubes()}")

    cc = ConwayCubes("data/day17_input.txt", 4)
    for n in range(6):
        cc.step()
    print(f"Part 2: {cc.active_cubes()}")

