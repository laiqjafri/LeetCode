# 53. Maximum Subarray
# Easy
#
# 12795
#
# 610
#
# Add to List
#
# Share
# Given an integer array nums,
# find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
#
#
# Example 1:
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:
#
# Input: nums = [1]
# Output: 1
# Example 3:
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -105 <= nums[i] <= 105
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = max_ = nums[0]

        for num in nums[1:]:
            curr_max = max(num, num + curr_max)
            max_ = max(max_, curr_max)

        return max_
