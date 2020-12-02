import re

class PasswordRec:
    def __init__(self, first, second, letter, password):
        self.first = first
        self.second = second
        self.letter = letter
        self.password = password

    def __str__(self):
        return "%d-%d %s: %s" % (self.first, self.second, self.letter, self.password)

    def verify(self):
        count = 0
        for c in self.password:
            if c == self.letter:
                count += 1
        if (count >= self.first) & (count <= self.second):
            return True
        else:
            return False

    def verify2(self):
        if ((self.password[self.first-1] == self.letter) ^
            (self.password[self.second-1] == self.letter)):
            return True
        else:
            return False

class PasswordDb:
    PASSWD_RE = re.compile("([0-9]+)-([0-9]+) ([a-z]): (.*)")

    def __init__(self):
        self.records = []    # List of PasswordRec

    def load_file(self, filename):
        self.records = []
        f = open(filename, "r")
        for line in f.readlines():
            # process one line into a password entry
            m = PasswordDb.PASSWD_RE.match(line)
            if m:
                record = PasswordRec(int(m.group(1)), int(m.group(2)), m.group(3), m.group(4))
                self.records.append(record)
                # print(f"Stored: {record}")

    def num_records(self):
        return len(self.records)

    def num_valid(self):
        ok = 0
        for rec in self.records:
            if rec.verify():
                ok += 1

        return ok

    def num_valid2(self):
        ok = 0
        for rec in self.records:
            if rec.verify2():
                ok += 1

        return ok
