# 300. Longest Increasing Subsequence
# Medium
#
# 7728
#
# 168
#
# Add to List
#
# Share
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the
# order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
#
#
#
# Example 1:
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# Example 3:
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
# Constraints:
#
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104


import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        output = []

        for num in nums:
            # Find number of elements in output smaller than num
            idx = bisect.bisect_left(output, num)

            if idx == len(output):
                output.append(num)
            else:
                output[idx] = num

        return len(output)
