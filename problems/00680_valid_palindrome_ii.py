# 680. Valid Palindrome II
# Easy
#
# 2590
#
# 167
#
# Add to List
#
# Share
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
#
#
#
# Example 1:
#
# Input: s = "aba"
# Output: true
# Example 2:
#
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:
#
# Input: s = "abc"
# Output: false


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                one, two = s[l:r], s[l+1:r+1]
                return one == one[::-1] or two == two[::-1]

            l, r = l + 1, r - 1

        return True
