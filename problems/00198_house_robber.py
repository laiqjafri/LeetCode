# 198. House Robber
# Medium
#
# 7080
#
# 197
#
# Add to List
#
# Share
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
# rob tonight without alerting the police.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
from typing import List


class Solution:
    def rob(self, nums: List[int], i=0, memo=None) -> int:
        if i >= len(nums):
            return 0

        if memo is None:
            memo = {}
        elif i in memo:
            return memo[i]

        memo[i] = max(self.rob(nums, i + 1, memo), self.rob(nums, i + 2, memo) + nums[i])
        return memo[i]
        # dp = [0] * (len(nums) + 1)
        # dp[-1], dp[-2] = 0, nums[-1]
        #
        # for i in range(len(nums) - 2, -1, -1):
        #     dp[i] = max(dp[i + 1], dp[i+2] + nums[i])
        #
        # return dp[0]
