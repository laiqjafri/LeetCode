# 31. Next Permutation
# Medium
#
# 5520
#
# 1886
#
# Add to List
#
# Share
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
#
# The replacement must be in place and use only constant extra memory.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:
#
# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:
#
# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:
#
# Input: nums = [1]
# Output: [1]
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1, 5, 8, 4, 7, 6, 5, 3, 1]
        # i = 3
        # j = 6

        # https://leetcode.com/media/original_images/31_Next_Permutation.gif

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
