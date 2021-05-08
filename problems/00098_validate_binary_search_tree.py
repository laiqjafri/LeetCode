# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
# Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode, min_=float("-inf"), max_=float("inf")) -> bool:
        return (
                   not root
               ) or (
                min_ < root.val < max_ and
                self.isValidBST(root.left, min_, root.val) and
                self.isValidBST(root.right, root.val, max_)
        )

    # def isValidBST(self, root: TreeNode, min_=float("-inf"), max_=float("inf")) -> bool:
    #     is_valid = True
    #     last_traversed = float("-inf")
    #
    #     def recurse(node):
    #         nonlocal is_valid
    #         nonlocal last_traversed
    #         if node and is_valid:
    #             recurse(node.left)
    #             if node.val <= last_traversed:
    #                 is_valid = False
    #             else:
    #                 last_traversed = node.val
    #             recurse(node.right)
    #
    #     recurse(root)
    #     return is_valid

    # def isValidBST(self, root: TreeNode, upper = float('inf'), lower = float('-inf')) -> bool:
    #     if not root:
    #         return True
    #
    #     if not lower < root.val < upper:
    #         return False
    #
    #     if not self.isValidBST(root.left, root.val, lower):
    #         return False
    #
    #     if not self.isValidBST(root.right, upper, root.val):
    #         return False
    #
    #     return True
