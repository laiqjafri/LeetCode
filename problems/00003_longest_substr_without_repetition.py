# Given a string s, find the length of the longest substring without repeating characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:
#
# Input: s = ""
# Output: 0


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        left = -1
        max_length = 0
        str_map = {}

        for index, char in enumerate(s):
            if str_map.get(char) is not None:
                # Max because of multiple repeating characters
                # E.g. "abba", here you want the index of last repeating element and not a's index
                left = max(left, str_map.get(char))

            max_length = max(index - left, max_length)
            str_map[char] = index

        return max_length


print(Solution().length_of_longest_substring("abba"))
print(Solution().length_of_longest_substring("abcabcbb"))
print(Solution().length_of_longest_substring("pwwkew"))
print(Solution().length_of_longest_substring("bbbbb"))
print(Solution().length_of_longest_substring(" "))
print(Solution().length_of_longest_substring("au"))
