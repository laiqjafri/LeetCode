# 179. Largest Number
# Medium
#
# 3062
#
# 319
#
# Add to List
#
# Share
# Given a list of non-negative integers nums, arrange them such that they form the largest number.
#
# Note: The result may be very large, so you need to return a string instead of an integer.
#
#
#
# Example 1:
#
# Input: nums = [10,2]
# Output: "210"
# Example 2:
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
# Example 3:
#
# Input: nums = [1]
# Output: "1"
# Example 4:
#
# Input: nums = [10]
# Output: "10"
from typing import List


class Comparator(str):
    def __lt__(self, other):
        return (self + other) > (other + self)


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(not num for num in nums):
            return '0'
        return "".join(sorted((str(num) for num in nums), key=Comparator))
