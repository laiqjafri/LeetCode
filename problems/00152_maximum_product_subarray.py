# 152. Maximum Product Subarray
# Medium
#
# 6775
#
# 225
#
# Add to List
#
# Share
# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
#
# It is guaranteed that the answer will fit in a 32-bit integer.
#
# A subarray is a contiguous subsequence of the array.
#
#
#
# Example 1:
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        final_max = nums[0]
        current_max = nums[0]
        current_min = nums[0]

        for num in nums[1:]:
            temp = current_max
            current_max = max(temp * num, current_min * num, num)
            current_min = min(temp * num, current_min * num, num)

            final_max = max(current_max, final_max)

        return final_max
