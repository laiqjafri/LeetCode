# 110. Balanced Binary Tree
# Easy
#
# 3398
#
# 225
#
# Add to List
#
# Share
# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: true
# Example 2:
#
#
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:
#
# Input: root = []
# Output: true


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def depth(node, curr_depth):
            if not node:
                return curr_depth

            return max(depth(node.left, curr_depth + 1), depth(node.right, curr_depth + 1))

        return abs(depth(root.left, 0) - depth(root.right, 0)) < 2 and \
               self.isBalanced(root.left) and \
               self.isBalanced(root.right)
