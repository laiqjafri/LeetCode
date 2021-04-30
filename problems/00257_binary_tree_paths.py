# 257. Binary Tree Paths
# Easy
#
# 2497
#
# 129
#
# Add to List
#
# Share
# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:
#
# Input: root = [1]
# Output: ["1"]


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        paths = []

        def recurse(node, path):
            path = list(path) + [str(node.val)]
            if not node.left and not node.right:
                paths.append(path)
            elif node.left and not node.right:
                recurse(node.left, path)
            elif node.right and not node.left:
                recurse(node.right, path)
            else:
                recurse(node.left, path)
                recurse(node.right, path)

        recurse(root, [])
        return ["->".join(path) for path in paths]
