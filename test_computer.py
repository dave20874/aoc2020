import pytest
from computer import Computer

def test_load():
    comp = Computer("data/day8_example1.txt")
    assert len(comp.code) == 9         # Verify 9 instructions loaded
    assert comp.code[5][0] == 'acc'    # Verify an opcode and arguments
    assert comp.code[5][1] == -99
    assert comp.ip == 0                # Verify reset condition after load
    assert comp.acc == 0


def test_reset():
    comp = Computer("data/day8_example1.txt")
    comp.ip = 100            # Modify state away from reset condition
    comp.acc = 99
    comp.reset()             # Reset the computer
    assert comp.ip == 0      # Verify reset conditions re-established
    assert comp.acc == 0

def test_nop():
    comp = Computer("data/day8_example1.txt")
    comp.step()             # First instruction of example 1 is the NOP
    assert comp.ip == 1     # Verify IP updated by one
    assert comp.acc == 0    # Verify accumulator didn't change

def test_acc():
    comp = Computer("data/day8_example1.txt")
    comp.step()
    comp.step()             # Second instruction of example1 is ACC
    assert comp.ip == 2     # Verify IP is now on 2
    assert comp.acc == 1    # Verify accumulator got updated

def test_jmp():
    comp = Computer("data/day8_example1.txt")
    comp.step()
    comp.step()
    comp.step()             # Third instruction of example 1 is JMP
    assert comp.ip == 6     # Verify IP changed as expected
    assert comp.acc == 1    # Verify Accumulator unchanged from prev instr.

def test_run_to_repeat():
    comp = Computer("data/day8_example1.txt")
    assert comp.runToRepeat() == 5
    assert comp.acc == 5
    assert comp.ip == 1

def test_run_to_repeat():
    comp = Computer("data/day8_example1.txt")
    assert comp.runToRepeat() == False   # call runToRepeat, verify returns False (didn't halt)
    assert comp.acc == 5    # Expected accumulator is 5 for example1 at repeat
    assert comp.ip == 1     # Expected IP is 1 for example1 at repeat

def test_run_to_halt():
    comp = Computer("data/day8_example1.txt")
    comp.ip = 8                         # Force IP to 8 so we accumulate once and halt
    assert comp.runToRepeat() == True   # Verify we saw halt condition
    assert comp.acc == 6                # Expected acc in this scenario: 6
    assert comp.ip == 9                 # Expected IP: just past loaded code.

def test_fix_loop():
    comp = Computer("data/day8_example1.txt")
    comp.fixLoop()                      # Try patching JMP and NOPs until it halts.
    assert comp.acc == 8                # When it works right on example1, we should get 8
    assert comp.ip == 9                 # When it halts, we should be past code.
