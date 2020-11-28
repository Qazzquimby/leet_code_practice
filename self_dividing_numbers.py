import typing as t


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> t.List[int]:
        return self_dividing_numbers(left, right)


def self_dividing_numbers(left: int, right: int) -> t.List[int]:
    digits = [int(digit) for digit in str(left)]
    if 0 not in digits and all([left % digit == 0 for digit in digits]):
        return [left]
    else:
        return []
