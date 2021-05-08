# 67. Add Binary
# Easy
#
# 2763
#
# 344
#
# Add to List
#
# Share
# Given two binary strings a and b, return their sum as a binary string.
#
#
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)

        carry = 0

        result = ""

        for x, y in zip(a[::-1], b[::-1]):
            result = str((int(x) + int(y) + carry) % 2) + result
            carry = 1 if (int(x) + int(y) + carry) > 1 else 0

        if carry:
            result = str(carry) + result

        return result