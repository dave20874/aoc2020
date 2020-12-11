class Seating:
    DIRECTIONS = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

    def __init__(self, filename):
        self.filename = filename
        self.occupied = {}
        self.is_seat = {}
        self.neighbors = {}

        self.load()

    def reset(self):
        self.occupied = {}
        self.neighbors = {}

    # Load in input file
    def load(self):
        self.reset()
        self.max_x = 0
        self.max_y = 0
        with open(self.filename) as f:
            for y, l in enumerate(f):
                if y > self.max_y:
                    self.max_y = y
                for x, c in enumerate(l.strip()):
                    if x > self.max_x:
                        self.max_x = x
                    if c == 'L':
                        self.is_seat[(x, y)] = True

    def comp_neighbors(self, adjacent=True):
        for coord in self.is_seat:
            neighbors = []
            for dx, dy in Seating.DIRECTIONS:
                # Look for neighboring seats in that direction until we find one or we
                # fall off the map
                terminate = False
                other = coord
                while not terminate:
                    other = (other[0]+dx, other[1]+dy)
                    if other in self.is_seat:
                        # We found a neighboring seat
                        neighbors.append(other)
                        terminate = True
                    elif ((other[0] < 0) | (other[0] > self.max_x) |
                          (other[1] < 0) | (other[1] > self.max_y)):
                        # We walked off the grid
                        terminate = True

                    if adjacent:
                        # If adjacent flag is set, don't look more than one step away.
                        terminate = True

            self.neighbors[coord] = neighbors

    def check_neighbors(self, coord, adjacent=True):
        count = 0
        for neighbor_coord in self.neighbors[coord]:
            if neighbor_coord in self.occupied:
                count += 1

        return count

    # Run one time step, return True if stable (nothing changed)
    def step(self, threshold=4):
        changed = False
        new_occupancy = {}
        for coord in self.is_seat:
            num_occupied = self.check_neighbors(coord)
            if num_occupied == 0:
                # No occupied neighbors: this becomes occupied
                new_occupancy[coord] = True
            elif num_occupied >= threshold:
                # Becomes unoccupied (nothing added to new_occupancy)
                pass
            elif coord in self.occupied:
                # Stays occupied because it was before
                new_occupancy[coord] = True

            # Note whether this is a change
            if (coord in new_occupancy) ^ (coord in self.occupied):
                changed = True

        # Adopt the new occupancy
        self.occupied = new_occupancy

        return not changed

    def num_occupied(self):
        return len(self.occupied)

    def show(self):
        print()
        for y in range(self.max_y + 1):
            for x in range(self.max_x+1):
                if (x, y) in self.occupied:
                    print('#', end="")
                elif (x, y) in self.is_seat:
                    print('L', end="")
                else:
                    print('.', end="")
            print()


    # Solve part 1
    def part1(self):
        self.reset()
        self.comp_neighbors(adjacent=True)
        stable = False
        while not stable:
            # self.show()
            stable = self.step()

        return self.num_occupied()

    # Solve part 2
    def part2(self):
        self.reset()
        self.comp_neighbors(adjacent=False)
        stable = False
        while not stable:
            # self.show()
            stable = self.step(threshold=5)

        return self.num_occupied()

if __name__ == '__main__':
    seating = Seating("data/day11_example1.txt")
    print(f"Day 11, Part 1: {seating.part1()}")
    print(f"Day 11, Part 2: {seating.part2()}")