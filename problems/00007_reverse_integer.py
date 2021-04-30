# 7. Reverse Integer
# Easy
#
# 4512
#
# 6913
#
# Add to List
#
# Share
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#
#
# Example 1:
#
# Input: x = 123
# Output: 321
# Example 2:
#
# Input: x = -123
# Output: -321
# Example 3:
#
# Input: x = 120
# Output: 21
# Example 4:
#
# Input: x = 0
# Output: 0


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = x * sign
        rev = []
        ret = 0

        while x > 0:
            rev.append(x % 10)
            x //= 10

        for index, digit in enumerate(reversed(rev)):
            ret += (digit * (10 ** index))

        ret *= sign

        if -(2 ** 31) <= ret <= ((2 ** 31) - 1):
            return ret
        else:
            return 0


print(Solution().reverse(1534236469))