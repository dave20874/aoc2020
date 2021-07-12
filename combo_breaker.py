class ComboBreaker:
    def __init__(self, filename):
        self.base = 7
        self.modulus = 20201227
        self.load(filename)

    def load(self, filename):
        with open(filename) as f:
            self.pubkey1 = int(f.readline().strip())
            self.pubkey2 = int(f.readline().strip())

    def get_smaller_loop_size(self):
        n = 1
        result = self.base
        while (result != self.pubkey1) & (result != self.pubkey2):
            result *= self.base
            result = result % self.modulus
            n += 1

        if result == self.pubkey1:
            print(f"Got pubkey 1, {result} with n={n}")
            return 1, n
        else:
            print(f"Got pubkey 2, {result} with n={n}")
            return 2, n

    def get_session_key(self, known_key, loop_size):
        if known_key == 1:
            base = self.pubkey2
        else:
            base = self.pubkey1

        result = 1
        for n in range(loop_size):
            result *= base
            result = result % self.modulus

        return result

    def part1(self):
        key, loop_size = self.get_smaller_loop_size()
        session_key = self.get_session_key(key, loop_size)

        return session_key

    def part2(self):
        # No part 2.
        return 0

if __name__ == '__main__':
    cb = ComboBreaker("data/day25_input.txt")
    key, loop_size = cb.get_smaller_loop_size()
    session_key = cb.get_session_key(key, loop_size)
    print(f"Session key: {session_key}")
