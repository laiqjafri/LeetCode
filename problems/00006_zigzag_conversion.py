# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
#
#
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:
#
# Input: s = "A", numRows = 1
# Output: "A"


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        arr = [[] for _ in range(numRows)]

        curr_row = 0
        curr_dir = "down"
        idx = 0

        while idx < len(s):
            if curr_dir == "down":
                if curr_row < numRows:
                    arr[curr_row].append(s[idx])
                    idx += 1
                    curr_row += 1
                else:
                    curr_dir = "up"
                    curr_row -= 2
            else:
                if curr_row > 0:
                    for i in range(numRows):
                        if i == curr_row:
                            arr[i].append(s[idx])
                            idx += 1
                        else:
                            arr[i].append(None)
                    curr_row -= 1
                else:
                    curr_dir = "down"

        return "".join([c for row in arr for c in row if c is not None])


print(Solution().convert("PAYPALISHIRING", 3))