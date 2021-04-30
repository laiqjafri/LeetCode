# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        numbers_map = {}

        for index, n in enumerate(nums):
            rem = numbers_map.get(target - n)
            if rem is not None and rem != index:
                return [index, rem]

            numbers_map[n] = index


print(Solution().two_sum([2, 7, 11, 15], 9))


def numberOfWays(arr, k):
    # Write your code here
    count_map = {}
    count = 0
    for v in arr:
        if count_map.get(v) is not None:
            count_map[v] = count_map[v] + 1
        else:
            count_map[v] = 1

    for v in count_map:
        diff = k - v
        if v == diff:
            if count_map[v] > 1:
                count += (count_map[v] * (count_map[v] - 1))
        else:
            count += count_map[diff]

    return count // 2

k_1 = 6
arr_1 = [1, 2, 3, 4, 3]
expected_1 = 2
output_1 = numberOfWays(arr_1, k_1)
