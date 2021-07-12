from lobby_layout import LobbyLayout


def test_load():
    ll = LobbyLayout("data/day24_example1.txt")
    assert len(ll.instructions) == 20


def test_part1():
    ll = LobbyLayout("data/day24_example1.txt")
    ll.run()
    assert ll.count_black() == 10


def test_new_coord():
    tests = (((0, 0), 0, (1, 0)),
             ((0, 0), 1, (0, -1)),
             ((0, 0), 2, (-1, -1)),
             ((0, 0), 3, (-1, 0)),
             ((0, 0), 4, (-1, 1)),
             ((0, 0), 5, (0, 1)),
             ((0, 1), 0, (1, 1)),
             ((0, 1), 1, (1, 0)),
             ((0, 1), 2, (0, 0)),
             ((0, 1), 3, (-1, 1)),
             ((0, 1), 4, (0, 2)),
             ((0, 1), 5, (1, 2)),
             )
    ll = LobbyLayout("data/day24_example1.txt")
    for start, dir, end in tests:
        actual = ll.new_coord(start, dir)
        assert actual == end
