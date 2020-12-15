class Recitation:
    def __init__(self, filename):
        self.start_seq = []
        self.last_spoken = {}
        self.turns = 0
        self.last = 0
        self.load(filename)

    def reset(self):
        self.last_spoken = {}
        self.turns = 0
        self.last = 0
        self.next = 0

    def load(self, filename):
        self.reset()
        with open(filename) as f:
            l = f.readline()
            for token in l.split(','):
                self.start_seq.append(int(token))

    def start(self):
        self.reset()
        for n in self.start_seq:
            self.turns += 1
            self.last_spoken[n] = self.turns
            self.last = n
        self.next = 0

    def play(self):
        played = self.next
        self.turns += 1
        if played in self.last_spoken:
            self.next = self.turns - self.last_spoken[played]
        else:
            self.next = 0

        self.last_spoken[played] = self.turns

        # print(f"{self.turns} : {played}")
        return played

    def play_to(self, turn, verbose=False):
        assert turn >= self.turns
        while self.turns < turn:
            n = self.play()
            if (verbose):
                print(f"{self.turns} {n}")

        return n






if __name__ == '__main__':
    rec = Recitation("data/day15_input.txt")
    rec.start()
    lim = 2020
    print(f"{lim}th play: {rec.play_to(lim, verbose=True)}")
