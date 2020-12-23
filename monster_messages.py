import re

class Rule:
    RULE_RE = re.compile("([0-9]+): (.*)")

    def __init__(self, definition):
        self.id = None
        self.definition = None
        self.literal = None      # literal character, if any
        self.a = None            # part of definition before pipe (or whole def if no pipe)
        self.b = None            # part of definition after pipe

        m = Rule.RULE_RE.match(definition)
        if m:
            self.id = int(m.group(1))
            self.definition = m.group(2)

            # print(f"id: {self.id} def'n: {self.definition}")
            if '"' in self.definition:
                self.literal = self.definition[1]
                # print(f"    literal {self.literal}")
            else:
                if '|' in self.definition:
                    parts = self.definition.split('|')
                    self.a = [int(x) for x in parts[0].split()]
                    self.b = [int(x) for x in parts[1].split()]
                    # print(f"    {self.a} | {self.b}")
                else:
                    self.a = [int(x) for x in self.definition.split()]
                    # print(f"    {self.a}")

    # Form the regular expression for a sequence of sub-rules
    def seq_re(self, ruleset, l):
        r = ""
        for id in l:
            r += ruleset[id].form_re(ruleset)

        return r

    # Form the regular expression for this rule
    def form_re(self, ruleset):
        retval = None
        if self.literal:
            retval = self.literal
        elif self.b is not None:
            # Compound
            retval = "(?:"+self.seq_re(ruleset, self.a)+"|"+self.seq_re(ruleset, self.b)+")"
        else:
            # Simple sequence
            retval = self.seq_re(ruleset, self.a)

        # print(f"{self.definition} -> {retval}")
        return retval

class MonsterMessages:
    def __init__(self, filename):
        self.filename = filename
        self.rules = {}
        self.messages = []

        self.load()

    def load(self):
        stage = "rules"
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.strip()
                if len(line) == 0:
                    stage = "messages"
                elif stage == "rules":
                    rule = Rule(line)
                    self.rules[rule.id] = rule
                elif stage == "messages":
                    self.messages.append(line)

    # Count the number of messages that match rule 0
    def num_match(self):
        # Form regular expression to match rule 0
        rule0_re = re.compile("^"+self.rules[0].form_re(self.rules)+"$")

        count = 0
        for m in self.messages:
            if rule0_re.match(m):
                # print(f"match: {m}")
                count += 1
            else:
                # print(f"non-match: {m}")
                pass

        return count

    # Count the number of messages that match a modified rule 0.
    # This amounts to recognizing the pattern (42+)(31+) and then
    # verifying that the number of 42s is greater than the number of 31s.
    def part2(self):
        part2_re = re.compile("^("+self.rules[42].form_re(self.rules)+"+)("+
                                   self.rules[31].form_re(self.rules)+"+)$")
        re_42 = re.compile(self.rules[42].form_re(self.rules))
        re_31 = re.compile(self.rules[31].form_re(self.rules))

        count = 0
        for msg in self.messages:
            m = part2_re.match(msg)
            if m:
                # print(f"    Msg: {msg}")
                prefix_42s = m.group(1)
                # print(f"    Prefix: {prefix_42s}")
                suffix_31s = m.group(2)
                # print(f"    Suffix: {suffix_31s}")

                # count 42s and 31s
                all_42s = re_42.findall(prefix_42s)
                # print(f"    42s: {all_42s}")
                num_42s = len(all_42s)

                all_31s = re_31.findall(suffix_31s)
                # print(f"    31s: {all_31s}")
                num_31s = len(all_31s)

                # print(f"Matched.  {num_42s} 42s, {num_31s} 31s")
                # If the 42's outnumber 31's, we're good.
                if num_42s > num_31s:
                    count += 1

            else:
                # print(f"non-match.")
                pass

        # Form special regular expression
        return count

if __name__ == '__main__':
    mm = MonsterMessages("data/day19_input.txt")
    print(f"Matches: {mm.num_match()}")
    print(f"Part 2: {mm.part2()}")
