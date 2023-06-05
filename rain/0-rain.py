#!/usr/bin/python3
"""
Rain
"""


def rain(walls):
    """
    This program calculates the amount
    of rainwater that can be retained
    after it rains
    """
    if not walls:
        return 0

    total_water = 0
    left_max = [0] * len(walls)
    right_max = [0] * len(walls)

    left_max[0] = walls[0]
    for i in range(1, len(walls)):
        left_max[i] = max(left_max[i-1], walls[i])

    right_max[-1] = walls[-1]
    for i in range(len(walls)-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])

    for i in range(len(walls)):
        water_height = min(left_max[i], right_max[i]) - walls[i]
        total_water += water_height

    return total_water
