# 1274. Number of Ships in a Rectangle
# Hard
#
# 180
#
# 29
#
# Add to List
#
# Share
# (This problem is an interactive problem.)
#
# Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.
#
# You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true If there is at least one ship in the rectangle represented by the two points, including on the boundary.
#
# Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are at most 10 ships in that rectangle.
#
# Submissions making more than 400 calls to hasShips will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.
#
#
#
# Example :
#
#
#
# Input:
# ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
# Output: 3
# Explanation: From [0,0] to [4,4] we can count 3 ships within the range.

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
       pass

class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def count(xs, ys):
            x, X = xs
            y, Y = ys
            if x > X or y > Y or not sea.hasShips(Point(X, Y), Point(x, y)):
                return 0

            if x == X and y == Y:
                return 1

            xm = (x + X) // 2
            ym = (y + Y) // 2

            xranges = (x, xm), (xm + 1, X)
            yranges = (y, ym), (ym + 1, Y)

            return sum(count(xr, yr) for xr in xranges for yr in yranges)

        return count((bottomLeft.x, topRight.x), (bottomLeft.y, topRight.y))
