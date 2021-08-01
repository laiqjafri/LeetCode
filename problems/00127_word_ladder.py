# 127. Word Ladder
# Hard
#
# 5611
#
# 1467
#
# Add to List
#
# Share
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
# beginWord -> s1 -> s2 -> ... -> sk such that:
#
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
# transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
#
#
#
# Example 1:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:
#
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
#
#
# Constraints:
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.


# Recursion, however time limit exceeds. No good way of memoizing
from collections import deque, defaultdict
from typing import List


class SolutionTimeLimitExceed:
    def is_at_distance_of_1(self, word1, word2):
        return sum(letter1 != letter2 for letter1, letter2 in zip(word1, word2)) == 1

    def ladderLength2(self, beginWord: str, endWord: str, wordList: List[str], trail=None, memo=None) -> int:
        if trail is None:
            trail = set()

        if memo is None:
            memo = {}
        elif (beginWord, endWord) in memo and memo[(beginWord, endWord)] <= len(trail):
            return memo[(beginWord, endWord)]

        if beginWord == endWord:
            return len(trail)

        if beginWord in trail:
            return float("inf")

        min_steps = float("inf")
        for word in wordList:
            if self.is_at_distance_of_1(beginWord, word):
                trail_copy = set(trail)
                trail_copy.add(beginWord)
                min_steps = min(min_steps, self.ladderLength2(word, endWord, wordList, trail_copy, memo))

        memo[(beginWord, endWord)] = min_steps
        return min_steps

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        steps = self.ladderLength2(beginWord, endWord, wordList)
        return 0 if steps == float("inf") else steps + 1


# Works like a charm
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str], trail=None, memo=None) -> int:
        intermediate_words_dict = defaultdict(list)

        for word in wordList:
            for i in range(len(beginWord)):
                intermediate_words_dict[word[:i] + "*" + word[i + 1:]].append(word)

        q = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)

        while q:
            curr_word, level = q.popleft()
            for i in range(len(curr_word)):
                intermediate_word = curr_word[:i] + "*" + curr_word[i + 1:]
                for word in intermediate_words_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1

                    if word not in visited:
                        visited.add(word)
                        q.append((word, level + 1))

        return 0
