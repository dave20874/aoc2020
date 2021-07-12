import re

class SimpleGame:
    def __init__(self, deck1, deck2):
        self.deck1 = deck1
        self.deck2 = deck2
        self.rounds = 0

    def play(self):
        assert len(self.deck1) > 0
        assert len(self.deck2) > 0
        card1 = self.deck1[0]
        self.deck1 = self.deck1[1:]
        card2 = self.deck2[0]
        self.deck2 = self.deck2[1:]
        if card1 > card2:
            # player 1 wins
            # print(f"{card1} beats {card2}, player 1 wins.")
            self.deck1.append(card1)
            self.deck1.append(card2)
        else:
            # player 2 wins
            # print(f"{card2} beats {card1}, player 2 wins.")
            self.deck2.append(card2)
            self.deck2.append(card1)
        self.rounds += 1

    # returns winner
    def play_to_end(self):
        while (len(self.deck1) > 0) & (len(self.deck2) > 0):
            self.play()

        if len(self.deck1) > 0:
            winner = 1
            deck = self.deck1
        else:
            winner = 2
            deck = self.deck2

        factor = len(deck)
        sum = 0
        for n in range(len(deck)):
            sum += deck[n] * factor
            factor -= 1

        return winner, sum

class RecursiveGame:
    def __init__(self, deck1, deck2):
        self.prev_decks = {}
        self.deck1 = deck1
        self.deck2 = deck2
        self.rounds = 0

    # returns 1 or 2 if a winner is decided, None otherwise.
    def play(self):
        # Check to see if this starting config has been seen before
        if seen_before:
            # Winner is player 1
            return 1


    # returns winner
    def play_to_end(self):
        prev_states = {}

        winner = None
        while (winner == None):
            # check for repetition
            state = (tuple(self.deck1), tuple(self.deck2))
            if state in prev_states:
                winner = 1
                break
            prev_states[state] = None

            # draw cards
            card1 = self.deck1[0]
            self.deck1 = self.deck1[1:]
            card2 = self.deck2[0]
            self.deck2 = self.deck2[1:]

            # if can recurse, recurse
            if (card1 <= len(self.deck1)) & (card2 <= len(self.deck2)):
                # play a recursive game
                subgame = RecursiveGame(self.deck1[:card1].copy(), self.deck2[:card2].copy())
                hand_winner, score = subgame.play_to_end()

            # else score normally.
            elif card1 > card2:
                hand_winner = 1

            else:
                hand_winner = 2

            # place cards in winning deck.
            if hand_winner == 1:
                self.deck1.append(card1)
                self.deck1.append(card2)
            else:
                self.deck2.append(card2)
                self.deck2.append(card1)

            # check for a game winner based on empty deck
            if len(self.deck1) == 0:
                winner = 2
            if len(self.deck2) == 0:
                winner = 1

        if winner == 1:
            deck = self.deck1
        else:
            deck = self.deck2

        factor = len(deck)
        sum = 0
        for n in range(len(deck)):
            sum += deck[n] * factor
            factor -= 1

        return winner, sum

class CrabCombat:
    def __init__(self, filename):
        self.filename = filename
        self.deck = {}   # deck[N] -> [top card, ..., bottom card]
        self.rounds = 0
        self.load()

    def load(self):
        player = 0
        player_re = re.compile("Player ([0-9]+):")
        card_re = re.compile("([0-9]+)")
        with open(self.filename) as f:
            for line in f.readlines():
                player_match = player_re.search(line)
                card_match = card_re.search(line)

                if player_match is not None:
                    player = int(player_match.group(1))
                    self.deck[player] = []
                elif card_match is not None:
                    card = int(card_match.group(1))
                    self.deck[player].append(card)

    def part1(self):
        game = SimpleGame(self.deck[1], self.deck[2])

        winner, score = game.play_to_end()

        return score

    def part2(self):
        game = RecursiveGame(self.deck[1], self.deck[2])

        winner, score = game.play_to_end()

        return score

if __name__ == '__main__':
    cc = CrabCombat("data/day22_input.txt")
    sum = cc.part1()
    print(f"Part1: {sum}")
