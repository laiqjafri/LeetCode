# 139. Word Break
# Medium
#
# 7493
#
# 354
#
# Add to List
#
# Share
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
#
#
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
#
# Constraints:
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str], memo=None) -> bool:
        if memo is None:
            memo = {}
        elif s in memo:
            return memo[s]

        if not s or s in wordDict:
            memo[s] = True
            return True

        for word in wordDict:
            if s.startswith(word):
                if self.wordBreak(s[len(word):], wordDict, memo):
                    memo[s] = True
                    return True

        memo[s] = False
        return False
