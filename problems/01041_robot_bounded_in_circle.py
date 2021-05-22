# 1041. Robot Bounded In Circle
# Medium
#
# 1234
#
# 348
#
# Add to List
#
# Share
# On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:
#
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degrees to the right.
# The robot performs the instructions given in order, and repeats them forever.
#
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
#
#
#
# Example 1:
#
# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
# Example 2:
#
# Input: instructions = "GG"
# Output: false
# Explanation: The robot moves north indefinitely.
# Example 3:
#
# Input: instructions = "GL"
# Output: true
# Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 'N'
        expected_directions = {
            'N': {'L': 'W', 'R': 'E'},
            'E': {'L': 'N', 'R': 'S'},
            'W': {'L': 'S', 'R': 'N'},
            'S': {'L': 'E', 'R': 'W'},
        }
        expected_movements = {
            'N': {'x':  0, 'y':  1},
            'E': {'x':  1, 'y':  0},
            'W': {'x': -1, 'y':  0},
            'S': {'x':  0, 'y': -1},
        }
        x = 0
        y = 0

        for instruction in instructions:
            if instruction is 'G':
                x += expected_movements[direction]['x']
                y += expected_movements[direction]['y']
            else:
                direction = expected_directions[direction][instruction]

        return (x is 0 and y is 0) or direction is not 'N'
