from boarding_pass import BoardingPass

def test_load():
    passes = BoardingPass("data/day5_example1.txt")
    assert len(passes.passes) == 3

def test_to_num():
    assert BoardingPass.to_num("BFFFBBFRRR") == 567
    assert BoardingPass.to_num("FFFBBBFRRR") == 119
    assert BoardingPass.to_num("BBFFBBFRLL") == 820

def test_find_max():
    passes = BoardingPass("data/day5_example1.txt")
    assert passes.find_max() == 820

