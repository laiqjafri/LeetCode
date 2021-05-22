# Circle and Lattice Points
# Given a circle of radius r in 2-D with origin or (0, 0) as center. The task is to find the total lattice points on circumference.
# Lattice Points are points with coordinates as integers in 2-D space.
#
# Example:
#
# Input  : r = 5.
# Output : 12
# Below are lattice points on a circle with
#     radius 5 and origin as (0, 0).
# (0,5), (0,-5), (5,0), (-5,0),
# (3,4), (-3,4), (-3,-4), (3,-4),
# (4,3), (-4,3), (-4,-3), (4,-3).
# are 12 lattice point.
import math


def circle_lattice_points(r: int) -> int:
    if not r:
        return 0

    result = 0

    for x in range(r):
        if int(math.sqrt((r ** 2) - (x ** 2))) ** 2 == r ** 2 - x ** 2:
            result += 4

    return result


print(circle_lattice_points(5))
