# 438. Find All Anagrams in a String
# Medium
#
# 4165
#
# 203
#
# Add to List
#
# Share
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)

        if len_s < len_p:
            return []

        counter_p = Counter(p)
        counter_s = {}

        output = []

        for i in range(len_s):
            counter_s[s[i]] = counter_s.get(s[i], 0) + 1

            if i >= len_p:
                if counter_s[s[i - len_p]] == 1:
                    del(counter_s[s[i - len_p]])
                else:
                    counter_s[s[i - len_p]] -= 1

            if counter_s == counter_p:
                output.append(i - len_p + 1)

        return output
