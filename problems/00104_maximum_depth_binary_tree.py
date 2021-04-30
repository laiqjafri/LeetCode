# 104. Maximum Depth of Binary Tree
# Easy
#
# 3767
#
# 95
#
# Add to List
#
# Share
# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:
#
# Input: root = [1,null,2]
# Output: 2
# Example 3:
#
# Input: root = []
# Output: 0
# Example 4:
#
# Input: root = [0]
# Output: 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode, depth=0) -> int:
        if not root:
            return depth

        return max(self.maxDepth(root.left, depth + 1), self.maxDepth(root.right, depth + 1))
