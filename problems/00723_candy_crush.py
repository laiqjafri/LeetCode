# This question is about implementing a basic elimination algorithm for Candy Crush.
#
# Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:
#
# If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
# After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
# After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
# If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
# You need to perform the above rules until the board becomes stable, then return the current board.
#
#
#
# Example:
#
# Input:
# board =
# [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
#
# Output:
# [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
#
# Explanation:
# https://assets.leetcode.com/uploads/2018/10/12/candy_crush_example_2.png
from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows = len(board)
        cols = len(board[0])

        crush = False

        for r in range(rows):
            for c in range(cols - 2):
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                    crush = True
                    board[r][c] = board[r][c+1] = board[r][c+2] = -(abs(board[r][c]))
        for r in range(rows - 2):
            for c in range(cols):
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                    crush = True
                    board[r][c] = board[r+1][c] = board[r+2][c] = -(abs(board[r][c]))

        if crush:
            for c in range(cols):
                index = rows - 1
                for r in range(rows-1, -1, -1):
                    if board[r][c] > 0:
                        board[index][c] = board[r][c]
                        index -= 1

                while index >= 0:
                    board[index][c] = 0
                    index -= 1
            return self.candyCrush(board)

        return board
