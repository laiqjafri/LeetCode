# 739. Daily Temperatures
# Medium
#
# 4298
#
# 130
#
# Add to List
#
# Share
# Given a list of daily temperatures temperatures, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
#
# For example, given the list of temperatures temperatures = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
# Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                curr = stack.pop()
                ans[curr] = i - curr
            stack.append(i)

        return ans