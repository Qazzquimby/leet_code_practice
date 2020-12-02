"""
An imminent hurricane threatens the coastal town of Codeville.
If at most two people can fit in a rescue boat, and the maximum weight limit for a given boat is k,
determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200,
the smallest number of boats required will be three.
"""
import typing as t


def get_min_boats(boat_limit: int, weights: t.List[int]) -> int:
    remaining_weights = sorted(weights, reverse=True)
    min_boats = 0

    while remaining_weights:
        first = remaining_weights[0]
        last = remaining_weights[-1]
        if first + last <= boat_limit:
            remaining_weights = remaining_weights[1:-1]
        else:
            remaining_weights = remaining_weights[1:]
        min_boats += 1

    return min_boats
