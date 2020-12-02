import tasks.boat_packing


def test_when_no_weights__0():
    actual = tasks.boat_packing.get_min_boats(100, [])
    expected = 0
    assert actual == expected


def test_when_2_people_under_weight__1():
    actual = tasks.boat_packing.get_min_boats(100, [20, 20])
    expected = 1
    assert actual == expected


def test_when_3_people_under_weight__2():
    actual = tasks.boat_packing.get_min_boats(100, [20, 20, 20])
    expected = 2
    assert actual == expected


def test_when_11_people_under_weight__6():
    actual = tasks.boat_packing.get_min_boats(100, [2] * 11)
    expected = 6
    assert actual == expected


def test_when_2_people_over_half_weight__2():
    actual = tasks.boat_packing.get_min_boats(100, [60, 60])
    expected = 2
    assert actual == expected


def test_when_3_people_over_half_weight__3():
    actual = tasks.boat_packing.get_min_boats(100, [60, 60, 60])
    expected = 3
    assert actual == expected


def test_when_60_40__1():
    actual = tasks.boat_packing.get_min_boats(100, [60, 40])
    expected = 1
    assert actual == expected


def test_when_60_60_40_40__2():
    actual = tasks.boat_packing.get_min_boats(100, [60, 40, 60, 40])
    expected = 2
    assert actual == expected
