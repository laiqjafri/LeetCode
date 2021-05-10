# 283. Move Zeroes
# Easy
#
# 5484
#
# 170
#
# Add to List
#
# Share
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
#
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
#
# Input: nums = [0]
# Output: [0]
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0

        for num in nums:
            if num:
                nums[i] = num
                i += 1

        nums[i:] = [0] * (len(nums) - i)