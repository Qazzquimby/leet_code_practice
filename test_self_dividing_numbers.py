import self_dividing_numbers


def test_when_left_right_1__return_1():
    actual = self_dividing_numbers.self_dividing_numbers(1, 1)
    expected = [1]
    assert expected == actual


def test_when_left_right_3__return_3():
    actual = self_dividing_numbers.self_dividing_numbers(3, 3)
    expected = [3]
    assert expected == actual


def test_when_left_right_10__return_empty():
    actual = self_dividing_numbers.self_dividing_numbers(10, 10)
    expected = []
    assert expected == actual


def test_when_left_right_11__return_1_1():
    actual = self_dividing_numbers.self_dividing_numbers(11, 11)
    expected = [11]
    assert expected == actual

# def test_when_left_right_13__return_empty():
#     actual = self_dividing_numbers.self_dividing_numbers(13, 13)
#     expected = []
#     assert expected == actual
