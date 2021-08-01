# 564. Find the Closest Palindrome
# Hard
#
# 391
#
# 1021
#
# Add to List
#
# Share
# Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome.
# If there is a tie, return the smaller one.
#
# The closest is defined as the absolute difference minimized between two integers.
#
#
#
# Example 1:
#
# Input: n = "123"
# Output: "121"
# Example 2:
#
# Input: n = "1"
# Output: "0"
# Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
#
#
# Constraints:
#
# 1 <= n.length <= 18
# n consists of only digits.
# n does not have leading zeros.
# n is representing an integer in the range [1, 1018 - 1].

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        n_len = len(n)

        candidates = set()

        for p in (n_len - 1, n_len):
            for diff in (-1, 1):
                candidates.add(10**p + diff)

        left_half = n[:(n_len + 1) // 2]

        for offset in (-1, 0, 1):
            left_half_candidate = str(int(left_half) + offset)
            candidates.add(
                int(
                    left_half_candidate + [left_half_candidate, left_half_candidate[:-1]][n_len & 1][::-1]
                )
            )

        candidates.discard(int(n))

        return str(min(
            candidates,
            key=lambda candidate: (abs(candidate - int(n)), candidate)
        ))
