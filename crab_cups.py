class CrabCups:
    def __init__(self, cups, augment_to=0):
        self.follows = {}
        current = None
        first = None
        for c in cups:
            n = int(c)
            if current is None:
                first = n
                self.min_entry = n
                self.max_entry = n
            else:
                self.follows[current] = n
                if n < self.min_entry:
                    self.min_entry = n
                if n > self.max_entry:
                    self.max_entry = n
            current = n

        if augment_to != 0:
            next = self.max_entry+1
            while current < augment_to:
                self.follows[current] = next
                current = next
                next = next + 1
            self.max_entry = augment_to

        self.follows[current] = first
        self.current = first

    def show(self):
        print(f"({self.current})", end="")

        n = self.follows[self.current]
        while n != self.current:
            print(f" {n}", end="")
            n = self.follows[n]
        print()

    def step(self):
        # identify entries that move
        rm1 = self.follows[self.current]
        rm2 = self.follows[rm1]
        rm3 = self.follows[rm2]
        tail = self.follows[rm3]
        removed = [rm1, rm2, rm3]
        # print(f"stepping, rm1:{rm1}, rm2:{rm2}, rm3:{rm3}, tail:{tail}")

        # Find insert point
        insert_pt = self.current - 1
        if insert_pt < self.min_entry:
            insert_pt = self.max_entry
        while insert_pt in removed:
            insert_pt -= 1
            if insert_pt < self.min_entry:
                insert_pt = self.max_entry

        # Move these entries
        self.follows[self.current] = tail
        self.follows[rm3] = self.follows[insert_pt]
        self.follows[insert_pt] = rm1

        # Update current
        self.current = tail

    def part1_sum(self):
        digit = 1
        sum = 0
        for n in range(8):
            sum *= 10
            digit = self.follows[digit]
            sum += digit

        return sum

    def part2_sum(self):
        value = 1
        sum = 1
        for n in range(2):
            value = self.follows[value]
            # print(f"value: {value}")
            sum *= value
        # print(f"product: {sum}")

        return sum

    def part1(self, iterations):
        for n in range(iterations):
            self.step()

        return self.part1_sum()

    def part2(self, iterations):
        for n in range(iterations):
            self.step()

        return self.part2_sum()

if __name__ == '__main__':
    cc = CrabCups("389125467", 1000000)
    # cc = CrabCups("156794823")
    # cc.show()
    sum = cc.part2(10000000)
    # cc.show()
    print(f"Sum: {sum}")