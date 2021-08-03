# 140. Word Break II
# Hard
#
# 3573
#
# 449
#
# Add to List
#
# Share
# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences in any order.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
#
#
# Example 1:
#
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]
# Example 2:
#
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
#
#
# Constraints:
#
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        output = []

        def wordBreakRecursive(s_, seen=None):
            if seen is None:
                seen = []

            if not s_:
                output.append(" ".join(seen))

            for word in wordDict:
                if s_.startswith(word):
                    wordBreakRecursive(s_[len(word):], list(seen + [word]))

        wordBreakRecursive(s)
        return output
