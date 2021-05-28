# 746. Min Cost Climbing Stairs
# Easy
#
# 3200
#
# 689
#
# Add to List
#
# Share
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.
#
#
#
# Example 1:
#
# Input: cost = [10,15,20]
# Output: 15
# Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
# Example 2:
#
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
#
#
# Constraints:
#
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int], i=None, memo=None) -> int:
        down_one = 0
        down_two = 0

        for i in range(2, len(cost) + 1):
            temp = down_one
            down_one = min(down_one + cost[i - 1], down_two + cost[i - 2])
            down_two = temp

        return down_one

# Recursion + Memoization
        # if i is None:
        #     i = len(cost)
        #
        # if memo is None:
        #     memo = {}
        # elif i in memo:
        #     return memo[i]
        #
        # if i <= 1:
        #     return 0
        #
        # memo[i] = min(
        #     cost[i - 1] + self.minCostClimbingStairs(cost, i - 1, memo),
        #     cost[i - 2] + self.minCostClimbingStairs(cost, i - 2, memo)
        # )
        #
        # return memo[i]
