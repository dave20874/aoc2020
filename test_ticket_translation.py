from ticket_translation import TicketInfo

def test_load():
    ti = TicketInfo("data/day16_example1.txt")
    assert len(ti.fields) == 3
    assert len(ti.nearby) == 4
    assert ti.mine[0] == 7
    assert ti.mine[1] == 1
    assert ti.mine[2] == 14

def test_scan():
    ti = TicketInfo("data/day16_example1.txt")
    assert ti.scan_err_rate() == 71

def test_id_fields():
    ti = TicketInfo("data/day16_example1.txt")

    # First discard the invalid tickets
    ti.scan_err_rate()

    # Second, figure out field assignments
    ti.id_fields()

    assert ti.fields["class"].index == 1
    assert ti.fields["row"].index == 0
    assert ti.fields["seat"].index == 2
