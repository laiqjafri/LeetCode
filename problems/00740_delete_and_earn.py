# 740. Delete and Earn
# Medium
#
# 1569
#
# 118
#
# Add to List
#
# Share
# Given an array nums of integers, you can perform operations on the array.
#
# In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.
#
# You start with 0 points. Return the maximum number of points you can earn by applying such operations.
#
#
#
# Example 1:
#
# Input: nums = [3,4,2]
# Output: 6
# Explanation: Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points.
# 6 total points are earned.
# Example 2:
#
# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
#
#
# Constraints:
#
# 1 <= nums.length <= 2 * 104
# 1 <= nums[i] <= 104
from typing import List


class Solution:
    def rob(self, nums, i=0, memo=None):
        if i >= len(nums):
            return 0

        if memo is None:
            memo = {}
        elif i in memo:
            return memo[i]

        memo[i] = max(self.rob(nums, i + 1, memo), self.rob(nums, i + 2, memo) + nums[i])
        return memo[i]

    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] * (max(nums) + 1)

        for num in nums:
            dp[num] += num

        return self.rob(dp)
