# 20. Valid Parentheses
# Easy
#
# 7983
#
# 326
#
# Add to List
#
# Share
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false
# Example 4:
#
# Input: s = "([)]"
# Output: false
# Example 5:
#
# Input: s = "{[]}"
# Output: true
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        map_ = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []

        for c in s:
            if c in map_.keys():
                if not stack or stack[-1] != map_.get(c):
                    return False
                else:
                    stack.pop()

            if c in map_.values():
                stack.append(c)

        return not stack
