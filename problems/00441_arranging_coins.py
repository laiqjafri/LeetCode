# 441. Arranging Coins
# Easy
#
# 965
#
# 801
#
# Add to List
#
# Share
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
#
# Given the integer n, return the number of complete rows of the staircase you will build.
#
#
#
# Example 1:
#
#
# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:
#
#
# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
#
#
# Constraints:
#
# 1 <= n <= 231 - 1


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 2:
            return 1

        k = 2
        left = 0
        right = n

        while left <= right:
            k = (left + right) // 2
            curr_n = (k * (k + 1)) / 2

            if curr_n == n:
                return k
            elif curr_n < n:
                left = k + 1
            else:
                right = k - 1

        return int(right)