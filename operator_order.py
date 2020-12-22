from collections.abc import Sequence

# Operates on a expression represented as a string.
class Expression:
    def __init__(self, text):
        self.text = text

    # Evaluate the expression using part 1 rules. (No operator precedence.)
    def eval1(self):
        accum = 0
        operation = None
        state = "start"
        stack = []
        for c in self.text:
            if c in "0123456789":
                val = int(c)
                if operation == '+':
                    accum += val
                    operation = None
                elif operation == '*':
                    accum *= val
                    operation = None
                else:
                    accum = val

            elif c == '(':
                stack.append((accum, operation))
                accum = 0
                operation = None
            elif c == ')':
                val = accum
                accum, operation = stack.pop(-1)
                if operation == '+':
                    accum += val
                    operation = None
                elif operation == '*':
                    accum *= val
                    operation = None
                else:
                    accum = val

            elif c == '+':
                operation = '+'

            elif c == '*':
                operation = '*'

        return accum

    # Parse a string expression into a nested list representation.
    # Assumes we are at the continuation of an expression.  We already have one operand and operator.
    # The job now is to collect second operand and operator, then recurse using proper precedence
    # between op1 and op2.
    def parse_cont(self, op1, term1, s, index, level):

        while index < len(self.text):
            c = self.text[index]
            # print(f" cont {level}: {c}")
            index += 1
            if c == '(':
                term2, index = self.parse_start(s, index, level+1)
            elif c == ')':
                # end of this sub-parser's job
                return [op1, term1, term2], index
            elif c in "0123456789":
                term2 = int(c)
                # print(f"    term2 = {term2}")
            elif c == '+':
                op2 = c
                if (op1 == '*') & (op2 == '+'):
                    # right-associative
                    right, index = self.parse_cont(op2, term2, s, index, level+1)
                    return [op1, term1, right], index
                else:
                    # left-associative
                    left = [op1, term1, term2]
                    return self.parse_cont(op2, left, s, index, level+1)

            elif c == '*':
                op2 = c
                if (op1 == '*') & (op2 == '+'):
                    # right-associative
                    right, index = self.parse_cont(op2, term2, s, index, level+1)
                    return [op1, term1, right], index
                else:
                    # left-associative
                    left = [op1, term1, term2]
                    return self.parse_cont(op2, left, s, index, level+1)

        return [op1, term1, term2], index

    # Parse a string expression into a nested list representation.
    # Assumes we are at the start of an expression.
    def parse_start(self, s, index, level=0):
        expr1 = None

        while index < len(self.text):
            c = self.text[index]
            # print(f"start {level}: {c}")
            index += 1
            if c == '(':
                # Restart with parenthetical expression
                expr1, index = self.parse_start(s, index, level+1)
            elif c == ')':
                # end of this sub-parser's job
                assert False
                return [], index+1
            elif c in "0123456789":
                # Catch this literal as expr1
                expr1 = int(c)
            elif c == '+':
                # Continue parsing from the state where we have one operand and one operator.
                return self.parse_cont('+', expr1, s, index, level+1)
            elif c == '*':
                # Continue parsing from the state where we have one operand and one operator.
                return self.parse_cont('*', expr1, s, index, level+1)
            else:
                # Whitespace and stuff we ignore
                pass

        return expr1, index

    # Evaluate a nested list representation of an expression, as generated by parse_start / parse_cont.
    def eval_expr(self, expr):
        # print(f"Expression: {expr}")
        op = expr[0]
        x1 = expr[1]
        x2 = expr[2]
        if isinstance(x1, Sequence):
            x1 = self.eval_expr(x1)
        if isinstance(x2, Sequence):
            x2 = self.eval_expr(x2)

        if op == '+':
            retval = x1 + x2
        elif op == '*':
            retval= x1 * x2
        else:
            assert False

        # print(f"    {retval}")
        return retval


    # Evaluation rules for part 2, uses parse_start and parse_cont helper functions.
    def eval2(self):
        # print(f"{self.text}")
        expr, index = self.parse_start(self.text, 0)

        return self.eval_expr(expr)

# Main class just loads up a list of Expression objects to evaluate with eval1 or eval2
class OperatorOrder:
    def __init__(self, filename):
        self.filename = filename
        self.expressions = []

        self.load()

    def load(self):
        with open(self.filename) as f:
            for line in f.readlines():
                self.expressions.append(Expression(line.strip()))

    def part1(self):
        sum = 0
        for e in self.expressions:
            sum += e.eval1()

        return sum

    def part2(self):
        sum = 0
        for e in self.expressions:
            sum += e.eval2()

        return sum

if __name__ == '__main__':
    oo = OperatorOrder("data/day18_input.txt")
    print(f"Day 18, part 2: {oo.part2()}")