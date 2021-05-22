# 264. Ugly Number II
# Medium
#
# 2637
#
# 160
#
# Add to List
#
# Share
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
#
# Given an integer n, return the nth ugly number.
#
#
#
# Example 1:
#
# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# Example 2:
#
# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        m2 = m3 = m5 = 1
        i = 2

        while n > 1:
            n2, n3, n5 = 2 * dp[m2], 3 * dp[m3], 5 * dp[m5]
            min_ = min(n2, n3, n5)

            if min_ == n2:
                m2 += 1
            if min_ == n3:
                m3 += 1
            if min_ == n5:
                m5 += 1

            dp[i] = min_
            i += 1
            n -= 1

        return dp[-1]
