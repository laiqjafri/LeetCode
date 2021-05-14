# 451. Sort Characters By Frequency
# Medium
#
# 2369
#
# 149
#
# Add to List
#
# Share
# Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.
#
#
#
# Example 1:
#
# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:
#
# Input: s = "cccaaa"
# Output: "aaaccc"
# Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:
#
# Input: s = "Aabb"
# Output: "bbAa"
# Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        # count = Counter(s)
        # return "".join(sorted(s, key=lambda c: (-count[c], ord(c))))
        return "".join([char * times for char, times in Counter(s).most_common()])
