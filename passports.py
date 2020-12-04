import re

class Passports():
    FIELDS = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")
    REQ_FIELDS = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    EYE_COLORS = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

    BYR_RE = re.compile("([0-9]{4})$")  # YYYY
    IYR_RE = re.compile("([0-9]{4})$")  # YYYY
    EYR_RE = re.compile("([0-9]{4})$")  # YYYY
    HGT_RE = re.compile("([0-9]+)([a-z]{2})$")  # N, aa (units)
    HCL_RE = re.compile("(#[0-9a-f]{6})$")  # #xxxxxx
    ECL_RE = re.compile("([a-z]{3})$")  # aaa
    PID_RE = re.compile("([0-9]{9})$")  # ddddddddd
    CID_RE = re.compile("(.*)$")

    FIELD_RE = {"byr": BYR_RE, "iyr": IYR_RE, "eyr": EYR_RE, "hgt": HGT_RE,
                "hcl": HCL_RE, "ecl": ECL_RE, "pid": PID_RE, "cid": CID_RE
                }

    def __init__(self, filename):
        self.filename = filename
        self.records = []

        # Map field name -> number of validation failures
        self.invalid = {}
        self.reset()

    def reset(self):
        # Map field name -> number of validation failures
        self.invalid = {"byr": 0, "iyr": 0, "eyr": 0, "hgt": 0, "hcl": 0, "ecl": 0, "pid": 0, "cid": 0}
        self.records = []
        self.load_file(self.filename)


    def load_file(self, filename):
        with open(filename) as f:
            cur_rec = {}
            for line in f:
                line = line.strip()
                fields = line.split()
                if len(fields) > 0:
                    # Process these fields into the current record.
                    for f in fields:
                        k, val = f.split(':')
                        cur_rec[k] = val
                else:
                    # Blank line : Store the completed record
                    self.records.append(cur_rec)
                    cur_rec = {}

        # Store that last in-progress record
        if len(cur_rec) > 0:
            self.records.append(cur_rec)

    def valid_byr(self, year):
        return (year >= 1920) & (year <= 2002)

    def valid_iyr(self, year):
        return (year >= 2010) & (year <= 2020)

    def valid_eyr(self, year):
        return (year >= 2020) & (year <= 2030)

    def valid_hgt(self, number, units):
        if units == "in":
            valid = (number >= 59) & (number <= 76)
        elif units == "cm":
            valid = (number >= 150) & (number <= 193)
        else:
            # invalid units
            valid = False

        return valid

    def valid_ecl(self, ecl):
        return ecl in Passports.EYE_COLORS

    def valid_field(self, record, field_name):
        valid = True

        # Access this record
        if field_name in record:
            value = record[field_name]

            m = Passports.FIELD_RE[field_name].match(value)
            if m is None:
                # Invalid format
                valid = False
            else:
                # Additional field-specific checks
                if field_name == "byr":
                    valid &= self.valid_byr(int(m.group(1)))
                elif field_name == "iyr":
                    valid &= self.valid_iyr(int(m.group(1)))
                elif field_name == "eyr":
                    valid &= self.valid_eyr(int(m.group(1)))
                elif field_name == "hgt":
                    valid &= self.valid_hgt(int(m.group(1)), m.group(2))
                elif field_name == "hcl":
                    # No further validation of hair color
                    pass
                elif field_name == "ecl":
                    valid &= self.valid_ecl(m.group(1))
                elif field_name == "pid":
                    # No further validation of hair color
                    pass
                elif field_name == "cid":
                    # No further validation of country id
                    pass

        if not valid:
            self.invalid[field_name] += 1

        # print(f"    {field_name} valid: {valid}")
        return valid

    def is_valid(self, record, check_fields=False):
        # Assume it's valid
        valid = True
        # print(f"Validating: {record}")

        # Must have all required fields
        for k in self.REQ_FIELDS:
            if k not in record:
                # A required field is missing
                # print(f"Invalid, missing field: {k}")
                valid = False

        if check_fields:
            # Apply validation rules to fields
            for field in Passports.FIELDS:
                valid &= self.valid_field(record, field)

        # print(f"    Valid: {valid}")
        return valid

    def validate(self, check_fields=False):
        self.reset()

        count = 0
        for rec in self.records:
            if self.is_valid(rec, check_fields):
                count += 1

        return count

