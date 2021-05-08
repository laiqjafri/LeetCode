# 953. Verifying an Alien Dictionary
# Easy
#
# 1690
#
# 695
#
# Add to List
#
# Share
# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.
#
#
#
# Example 1:
#
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:
#
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:
#
# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True

        mapping = {}
        for i, c in enumerate(order):
            mapping[c] = i

        def is_valid_order(word1, word2):
            for c1, c2 in zip(word1, word2):
                if mapping[c1] != mapping[c2]:
                    return mapping[c1] < mapping[c2]

            return len(word1) <= len(word2)

        for i in range(len(words) - 1):
            if not is_valid_order(words[i], words[i + 1]):
                return False

        return True
