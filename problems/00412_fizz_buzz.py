# 412. Fizz Buzz
# Easy
#
# 1443
#
# 1643
#
# Add to List
#
# Share
# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.
#
#
# Example 1:
#
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
#
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
#
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
#
#
# Constraints:
#
# 1 <= n <= 104
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        divisible_by_5 = lambda i: i % 5 == 0
        divisible_by_3 = lambda i: i % 3 == 0

        def toFizzBuzz(i):
            if divisible_by_5(i) and divisible_by_3(i):
                return "FizzBuzz"
            elif divisible_by_5(i):
                return "Buzz"
            elif divisible_by_3(i):
                return "Fizz"


            return str(i)

        return [toFizzBuzz(i) for i in range(1, n + 1)]
