# 15. 3Sum
# Medium
#
# 10408
#
# 1067
#
# Add to List
#
# Share
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
#
# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
#
# Input: nums = []
# Output: []
# Example 3:
#
# Input: nums = [0]
# Output: []
from typing import List


class Solution:
    def _twoSum(self, nums, target):
        map_ = set()
        for num in nums:
            if (target - num) in map_:
                yield target - num, num

            map_.add(num)


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        visited = set()

        for i, num in enumerate(nums):
            if num not in visited:
                for x, y in self._twoSum(nums[:i] + nums[i+1:], -num):
                    res.add(tuple(sorted([x, y, num])))

            visited.add(num)

        return res
