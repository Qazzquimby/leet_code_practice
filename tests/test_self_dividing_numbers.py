from tasks import self_dividing_numbers


def assert_returns_same_as_left(left: int, right: int):
    actual = self_dividing_numbers.self_dividing_numbers(left, right)
    expected = [left]
    assert expected == actual


def test_when_left_right_1__return_1():
    assert_returns_same_as_left(1, 1)


def test_when_left_right_3__return_3():
    assert_returns_same_as_left(3, 3)


def test_when_left_right_10__return_empty():
    actual = self_dividing_numbers.self_dividing_numbers(10, 10)
    expected = []
    assert expected == actual


def test_when_left_right_11__return_1_1():
    assert_returns_same_as_left(11, 11)


def test_when_left_right_13__return_empty():
    actual = self_dividing_numbers.self_dividing_numbers(13, 13)
    expected = []
    assert expected == actual


def test_when_1_9__return_1_through_9():
    actual = self_dividing_numbers.self_dividing_numbers(1, 9)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert expected == actual


def test_when_0_22():
    actual = self_dividing_numbers.self_dividing_numbers(0, 22)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert expected == actual
