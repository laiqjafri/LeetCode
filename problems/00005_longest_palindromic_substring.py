# Given a string s, return the longest palindromic substring in s.
#
#
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
# Example 3:
#
# Input: s = "a"
# Output: "a"
# Example 4:
#
# Input: s = "ac"
# Output: "a"

class Solution:
    def _expand_around_the_corners(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[(left + 1): right]

    def longest_palindrome(self, s: str) -> str:
        i = 0
        longest_palindrome_str = ""
        while i < len(s):
            s1 = self._expand_around_the_corners(s, i, i)
            s2 = self._expand_around_the_corners(s, i, i + 1)
            longer = s1 if len(s1) >= len(s2) else s2
            longest_palindrome_str = longest_palindrome_str if len(longest_palindrome_str) >= len(longer) else longer
            i += 1

        return longest_palindrome_str


print(Solution().longest_palindrome("cbbd"))
print(Solution().longest_palindrome("ac"))