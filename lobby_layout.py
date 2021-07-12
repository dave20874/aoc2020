class LobbyLayout:
    EAST = 0
    SOUTHEAST = 1
    SOUTHWEST = 2
    WEST = 3
    NORTHWEST = 4
    NORTHEAST = 5

    def __init__(self, filename):
        self.instructions = []
        self.tiles = {}    # (x,y) -> True for black tiles
        self.load(filename)

    def load(self, filename):
        with open(filename) as f:
            for line in f.readlines():
                l = len(line.strip())
                sequence = []
                cursor = 0
                while cursor < l:
                    c = line[cursor]
                    cursor += 1
                    if c == 'e':
                        # East
                        dir = LobbyLayout.EAST
                    elif c == 'w':
                        # West
                        dir = LobbyLayout.WEST
                    elif c == 'n':
                        c = line[cursor]
                        cursor += 1
                        if c == 'e':
                            # NE
                            dir = LobbyLayout.NORTHEAST
                        elif c == 'w':
                            # NW
                            dir = LobbyLayout.NORTHWEST
                    elif c == 's':
                        c = line[cursor]
                        cursor += 1
                        if c == 'e':
                            # SE
                            dir = LobbyLayout.SOUTHEAST
                        elif c == 'w':
                            # SW
                            dir = LobbyLayout.SOUTHWEST

                    sequence.append(dir)
                self.instructions.append(sequence)

    def new_coord(self, old_coord, step):
        if (old_coord[1] & 1) == 0:
            # Even Y rows, no X adjust if moving in Y
            x_adjust = 0
        else:
            # Odd Y rows, adjust X when moving in Y
            x_adjust = 1

        if step == LobbyLayout.EAST:
            coord = (old_coord[0] + 1, old_coord[1])
        elif step == LobbyLayout.WEST:
            coord = (old_coord[0] - 1, old_coord[1])
        elif step == LobbyLayout.SOUTHEAST:
            coord = (old_coord[0] + x_adjust, old_coord[1]-1)
        elif step == LobbyLayout.SOUTHWEST:
            coord = (old_coord[0] - 1 + x_adjust, old_coord[1]-1)
        elif step == LobbyLayout.NORTHEAST:
            coord = (old_coord[0] + x_adjust, old_coord[1]+1)
        elif step == LobbyLayout.NORTHWEST:
            coord = (old_coord[0] - 1 + x_adjust, old_coord[1]+1)

        return coord

    def run(self):
        for instruction in self.instructions:
            # find coord of tile to flip
            coord = (0, 0)
            for step in instruction:
                coord = self.new_coord(coord, step)
                # print(f"  Moved {step} to {coord}")

            # flip coord
            if coord in self.tiles:
                # Flip existing tile
                if self.tiles[coord]:
                    # Flip from black to white
                    self.tiles[coord] = False
                    # print(f"Flipped {coord} to White.")
                else:
                    # Flip from white to black
                    self.tiles[coord] = True
                    # print(f"Flipped {coord} to Black.")
            else:
                # Unregistered tile flips from white to black
                self.tiles[coord] = True
                # print(f"Started {coord} at Black.")

    def count_black(self):
        black_tiles = 0
        for coord in self.tiles:
            if self.tiles[coord]:
                black_tiles += 1

        return black_tiles

    def part1(self):
        self.run()
        return self.count_black()

    def black_neighbors(self, coord):
        count = 0
        for dir in (LobbyLayout.EAST, LobbyLayout.SOUTHEAST, LobbyLayout.SOUTHWEST,
                    LobbyLayout.WEST, LobbyLayout.NORTHWEST, LobbyLayout.NORTHEAST):
            neighbor = self.new_coord(coord, dir)
            if (neighbor in self.tiles) and self.tiles[neighbor]:
                count += 1

        return count

    def hex_life(self):
        # Create a list of cells to evaluate.  (The black tiles and their neighbors)
        eval_cells = {}
        for coord in self.tiles:
            if self.tiles[coord]:
                # A black cell
                eval_cells[coord] = True
                for dir in (LobbyLayout.EAST, LobbyLayout.SOUTHEAST, LobbyLayout.SOUTHWEST,
                            LobbyLayout.WEST, LobbyLayout.NORTHWEST, LobbyLayout.NORTHEAST):
                    neighbor = self.new_coord(coord, dir)
                    eval_cells[neighbor] = True

        # Evaluate all those cells, building a new set of black tiles
        next_tiles = {}
        for cell in eval_cells:
            n = self.black_neighbors(cell)
            if (cell in self.tiles) and (self.tiles[cell]):
                # A black cell.  It stays if 1 or 2 neighbors are black
                if n == 1 or n == 2:
                    next_tiles[cell] = True
            else:
                # A White cell.  Flip to black if exactly 2 black neighbors
                if n == 2:
                    next_tiles[cell] = True

        # Replace last generation with this one
        self.tiles = next_tiles

    def part2(self):
        self.run()
        n = self.count_black()
        print(f"Generation {0}: {n} black cells.")
        for gen in range(100):
            self.hex_life()
            n = self.count_black()
            print(f"Generation {gen+1}: {n} black cells.")

        return self.count_black()

if __name__ == '__main__':
    ll = LobbyLayout("data/day24_input.txt")
    print(f"Part 2: {ll.part2()}")
