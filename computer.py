class Computer:
    def __init__(self, filename):
        self.acc = 0            # Accumulator
        self.ip = 0             # Instruction pointer
        self.code = {}          # Addr -> instruction
        self.load(filename)     # Load the given file into code

    # Puts machine back in initial state
    def reset(self):
        self.acc = 0
        self.ip = 0

    # Loads code from file and resets
    def load(self, filename):
        with open(filename) as f:
            for addr, line in enumerate(f):
                opcode, arg = line.strip().split()
                self.code[addr] = (opcode, int(arg))

        self.reset()

    # Execute one instruction
    def step(self):
        opcode, arg = self.code[self.ip]
        next_ip = self.ip+1
        if opcode == 'nop':
            pass
        elif opcode == 'acc':
            self.acc += arg
        elif opcode == 'jmp':
            next_ip = self.ip + arg

        self.ip = next_ip

    # Execute instructions until we repeat one or until machine halts.
    # Halt is defined as a jump to instruction after the loaded code.
    def runToRepeat(self):
        # Instructions we've already executed
        executed = {}
        end_ip = len(self.code)

        while (self.ip != end_ip) & (self.ip not in executed):
            # Execute one instruction
            executed[self.ip] = True
            self.step()

        return self.ip == end_ip

    # Attempts to fix looping issue (Day 8, part 2) by changing a JMP to NOP or NOP to JMP.
    # It tries this change at all locations until it works.  (Code halts instead of loops.)
    # On success, machine is halted with accumulator reflecting last state.
    def fixLoop(self):
        patch_cursor = 0

        halted = False
        while not halted:
            # Find an instruction to modify
            orig_code = self.code[patch_cursor]

            if self.code[patch_cursor][0] == "nop":
                self.code[patch_cursor] = ("jmp", self.code[patch_cursor][1])
            elif self.code[patch_cursor][0] == "jmp":
                self.code[patch_cursor] = ("nop", self.code[patch_cursor][1])

            # Try running to see if we halt or repeat
            self.reset()
            halted = self.runToRepeat()

            # Unmodify that instruction
            self.code[patch_cursor] = orig_code

            patch_cursor += 1


