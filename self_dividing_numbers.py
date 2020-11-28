import typing as t


def self_dividing_numbers(left: int, right: int) -> t.List[int]:
    return [num for num in range(left, right + 1) if _is_self_dividing(num)]


def _is_self_dividing(num: int) -> bool:
    digits = [int(digit) for digit in str(num)]

    contains_0 = 0 in digits
    self_dividing = not contains_0 and all([num % digit == 0 for digit in digits])
    return self_dividing
