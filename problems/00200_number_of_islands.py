# 200. Number of Islands
# Medium
#
# 8162
#
# 241
#
# Add to List
#
# Share
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
#
#
# Example 1:
#
# Input: grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
#
# Input: grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]
# Output: 3
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_islands = 0

        def mark_cell(row, col):
            total_rows, total_cols = len(grid), len(grid[0])

            if row < 0 or row >= total_rows or col < 0 or col >= total_cols or grid[row][col] == '0':
                return


            grid[row][col] = '0'
            mark_cell(row, col - 1)
            mark_cell(row, col + 1)
            mark_cell(row - 1, col)
            mark_cell(row + 1, col)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    total_islands += 1
                    mark_cell(row, col)

        return total_islands
