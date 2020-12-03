class Forest:
    def __init__(self, filename):
        self.width = 0
        self.height = 0
        self.tree_at = {}
        with open(filename, "r") as f:
            for y, line in enumerate(f.readlines()):
                for x, c in enumerate(line.strip()):
                    if c == '#':
                        self.tree_at[(x, y)] = True
                    if x+1 > self.width:
                        self.width = x+1
                    if y+1 > self.height:
                        self.height = y+1

    def is_tree(self, x, y):
        # Wrap x,y to the first of the repeated grids in X
        x = x % self.width

        # If the key is in self.tree_at, there's a tree there.
        return ((x, y) in self.tree_at)

    def get_num_trees(self, dx, dy):
        count = 0
        x = 0
        y = 0
        while y < self.height:
            if self.is_tree(x, y):
                count += 1
            x += dx
            y += dy

        return count
