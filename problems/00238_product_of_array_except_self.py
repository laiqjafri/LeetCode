# 238. Product of Array Except Self
# Medium
#
# 7339
#
# 553
#
# Add to List
#
# Share
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
#
# Follow up:
#
# Could you solve it in O(n) time complexity and without using division?
# Could you solve it with O(1) constant space complexity? (The output array does not count as extra space for space complexity analysis.)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        R = 1
        for i in reversed(range(len(nums))):
            res[i] *= R
            R *= nums[i]

        return res