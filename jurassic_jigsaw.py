import re
import numpy as np

class Image:
    def __init__(self):
        self.orientation = 0
        self.w = 0
        self.h = 0
        self.data = {}

    def show(self):
        for x in range(self.h):
            for y in range(self.w):
                print(self.get_elt(x, y), end="")
            print()
        print()

    def load_lines(self, lines):
        self.w = len(lines[0])
        self.h = len(lines)
        for x in range(self.h):
            for y in range(self.w):
                self.data[(x, y)] = lines[x][y]

    def load_tiles(self, tiles, placements):
        # print(f"placements: {placements}")
        for position in placements:
            tile, orientation = placements[position]
            assert tile.image.orientation == orientation

            (tile_x, tile_y) = position
            # Copy tile's image data into self.data.
            for x in range(1, tile.image.h-1):
                for y in range(1, tile.image.w-1):
                    newx = tile_x * (tile.image.h-2) + (x-1)
                    newy = tile_y * (tile.image.w-2) + (y-1)
                    self.data[(newx, newy)] = tile.image.get_elt(x, y)

                    if newx >= self.h:
                        self.h = newx+1
                    if newy >= self.w:
                        self.w = newy+1
        self.orientation = 0

    def roughness(self):
        n = 0
        for elt in self.data:
            if self.data[elt] == '#':
                n += 1
        return n

    def set_orientation(self, orientation):
        self.orientation = orientation

    def orient(self, x, y):
        flipped = False
        rotations = self.orientation
        if rotations >= 4:
            flipped = True
            rotations -= 4

        cx, cy = self.h/2, self.w/2
        for n in range(rotations):
            x, y = y, self.w-1-x

        if flipped:
            y = self.w-1 - y

        return (x, y)

    def get_elt(self, x, y):
        coord = self.orient(x, y)
        return self.data[coord]

        return retval

    def get_top(self):
        s = ""
        for y in range(self.w):
            s += self.get_elt(0, y)
        return s

    def get_bottom(self):
        s = ""
        for y in range(self.w):
            s += self.get_elt(self.h-1, y)
        return s

    def get_left(self):
        s = ""
        for x in range(self.h):
            s += self.get_elt(x, 0)
        return s

    def get_right(self):
        s = ""
        for x in range(self.h):
            s += self.get_elt(x, self.w-1)
        return s

class Tile:
    def __init__(self, tile_no, lines):
        self.tile_no = tile_no
        # self.lines = lines
        self.image = Image()
        self.image.load_lines(lines)

        # print(f"Tile {self.tile_no}:")
        # self.image.show()

class JurassicJigsaw:
    ORIENTATIONS = (0, 1, 2, 3, 4, 5, 6, 7)

    def __init__(self, filename, w, h):
        self.filename = filename
        self.w = w
        self.h = h
        self.tiles = []

        self.load()

    def load(self):
        TILE_NO_RE = re.compile("Tile ([0-9]+):")
        with open(self.filename) as f:
            tile_no = None
            lines = []
            for l in f.readlines():
                l = l.strip()
                m = TILE_NO_RE.match(l)
                if m:
                    # Tile number
                    tile_no = int(m.group(1))
                elif len(l) == 0:
                    # end of tile
                    tile = Tile(tile_no, lines)
                    self.tiles.append(tile)
                    lines = []
                else:
                    # Tile data
                    lines.append(l)

            # get the last one
            tile = Tile(tile_no, lines)
            self.tiles.append(tile)

    def fits(self, placements, coord, tile):
        # If there's a tile above, make sure this tile matches
        if coord[0] > 0:
            mate_tile, mate_orientation = placements[(coord[0]-1, coord[1])]
            if tile.image.get_top() != mate_tile.image.get_bottom():
                # Not a match
                return False

        # If there's a tile to the left, make sure this tile matches
        if coord[1] > 0:
            mate_tile, mate_orientation = placements[coord[0], coord[1]-1]
            if tile.image.get_left() != mate_tile.image.get_right():
                # Not a match
                return False

        # No mismatches so it fits.
        return True

    def _solve(self, placements, placed, next_coord):
        # If next coord is past end, unwind recursion
        if next_coord[1] >= self.h:
            return placements

        # Try each tile, each orientation.
        # If the tile is available and it fits at next_coord, with the given orientation, place it and recurse.
        for tile in self.tiles:
            if tile.tile_no in placed:
                continue
            for orientation in JurassicJigsaw.ORIENTATIONS:
                tile.image.set_orientation(orientation)
                if self.fits(placements, next_coord, tile):
                    # print(f"Fitted {tile.tile_no} at {next_coord}, orientation {orientation}")
                    # recurse
                    placements[next_coord] = (tile, orientation)
                    now_placed = placed + (tile.tile_no,)
                    if next_coord[0]+1 >= self.w:
                        new_next_coord = (0, next_coord[1]+1)
                    else:
                        new_next_coord = (next_coord[0]+1, next_coord[1])
                    soln = self._solve(placements, now_placed, new_next_coord)

                    if soln is not None:
                        # Found a solution
                        return soln

                    # print(f"Unfitted {tile.tile_no}")
                    del placements[next_coord]

        # No solution found
        return None

    def solve(self):
        placements = {}   # map (x, y) -> (tile_no, orientation)
        placed = ()       # list of tile_no
        next_coord = (0, 0)
        soln = self._solve(placements, placed, next_coord)
        if soln is None:
            print("No solution!")
        return soln

    def part1(self):
        solution = self.solve()

        prod = 1
        for coord in ((0, 0), (0, self.w-1), (self.h-1, 0), (self.h-1, self.w-1)):
            tile, orientation = solution[coord]
            prod *= tile.tile_no
        # print(f"Solved: {prod}")
        return prod

    def search_monsters(self, image):
        MONSTER_H = 3
        MONSTER_W = 20
        monster_coords = ((1,0),(2,1),(2,4),(1,5),(1,6),(2,7),(2,10),(1,11),
                          (1,12),(2,13),(2,16),(1,17),(0,18),(1,18),(1,19))

        # print(f"Orientation: {image.orientation}")
        # image.show()

        monsters = 0
        m_elts = {}

        for x in range(image.h-MONSTER_H):
            for y in range(image.w-MONSTER_W):
                monster = True
                for c in monster_coords:
                    if image.get_elt(c[0]+x, c[1]+y) != '#':
                        monster = False
                        break

                if monster:
                    monsters += 1
                    # Put all the monster coordinates into a dict as keys.
                    # These coords will be subtracted from roughness
                    for c in monster_coords:
                        check_coord = (c[0] + x, c[1] + y)
                        m_elts[check_coord] = True

        return (monsters, len(m_elts))
        

    def part2(self):
        retval = 0
        placements = self.solve()
        image = Image()
        image.load_tiles(self.tiles, placements)
        # print("Tiles loaded.")
        for orientation in self.ORIENTATIONS:
            image.set_orientation(orientation)
            monsters, m_roughness = self.search_monsters(image)
            if monsters > 0:
                retval = image.roughness() - m_roughness
                # print(f"Roughness is {retval}")
                break

        return retval

if __name__ == '__main__':
    jj = JurassicJigsaw("data/day20_input.txt", 12, 12)
    # jj = JurassicJigsaw("data/day20_example1.txt", 3, 3)
    jj.part2()