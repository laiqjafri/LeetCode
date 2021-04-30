# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
#
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
from typing import List


class Solution:
    def find_median_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        idx1 = 0
        idx2 = 0

        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] <= nums2[idx2]:
                res.append(nums1[idx1])
                idx1 += 1
            else:
                res.append(nums2[idx2])
                idx2 += 1

        if idx1 != len(nums1):
            res += nums1[idx1:]

        if idx2 != len(nums2):
            res += nums2[idx2:]

        res_len = len(res)

        if res_len % 2 == 0:
            return (res[(res_len // 2) - 1] + res[res_len // 2]) / 2
        else:
            return res[res_len // 2]


print(Solution().find_median_sorted_arrays([1, 2], [3, 4]))
