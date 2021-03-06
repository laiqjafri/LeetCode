# 29. Divide Two Integers
# Medium
#
# 1785
#
# 6896
#
# Add to List
#
# Share
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
#
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.
#
#
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.
# Example 3:
#
# Input: dividend = 0, divisor = 1
# Output: 0
# Example 4:
#
# Input: dividend = 1, divisor = 1
# Output: 1


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend * divisor) >= 0

        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = 0

        while True:
            if dividend < divisor:
                break
            else:
                i, temp = 1, divisor
                while dividend >= temp * 2:
                    i *= 2
                    temp *= 2

            ans += i
            dividend -= temp

        ans = ans if positive else ans * -1
        if ans >= 2 ** 31: return (2 ** 31) - 1
        if ans < -(2 ** 31): return -(2 ** 31)

        return ans
