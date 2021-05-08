# 443. String Compression
# Medium
#
# 1288
#
# 3249
#
# Add to List
#
# Share
# Given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
#
#
# Follow up:
# Could you solve it using only O(1) extra space?
#
#
#
# Example 1:
#
# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:
#
# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.
# Example 3:
#
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
# Example 4:
#
# Input: chars = ["a","a","a","b","b","a","a"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","3","b","2","a","2"].
# Explanation: The groups are "aaa", "bb", and "aa". This compresses to "a3b2a2".
# Note that each group is independent even if two groups have the same character.
from typing import List


class Solution:
    def _write_code(self, chars, write, current_char, current_count):
        chars[write] = current_char
        write += 1
        if current_count > 1:
            for digit in str(current_count):
                chars[write] = digit
                write += 1
        return write

    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)

        write = 0
        current_count = 1
        current_char = chars[0]

        for index in range(1, len(chars)):
            if current_char == chars[index]:
                current_count += 1
            else:
                write = self._write_code(chars, write, current_char, current_count)
                current_count = 1
                current_char = chars[index]

        return self._write_code(chars, write, current_char, current_count)