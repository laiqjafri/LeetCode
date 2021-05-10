# 125. Valid Palindrome
# Easy
#
# 1970
#
# 3827
#
# Add to List
#
# Share
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
#
#
# Example 1:
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
            else:
                if not s[left].isalnum():
                    left += 1
                if not s[right].isalnum():
                    right -= 1
        return True
