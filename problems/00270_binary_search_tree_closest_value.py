# 270. Closest Binary Search Tree Value
# Easy
#
# 1046
#
# 76
#
# Add to List
#
# Share
# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
#
#
#
# Example 1:
#
#
# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4
# Example 2:
#
# Input: root = [1], target = 4.428571
# Output: 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val

        while root:
            closest = min(root.val, closest, key=lambda val: abs(target - val))
            root = root.left if target < root.val else root.right

        return closest