# 199. Binary Tree Right Side View
# Medium
#
# 3889
#
# 210
#
# Add to List
#
# Share
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
# Example 2:
#
# Input: root = [1,null,3]
# Output: [1,3]
# Example 3:
#
# Input: root = []
# Output: []
from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        depth_mapping = defaultdict(list)

        def recurse(node, depth):
            if node:
                recurse(node.left, depth + 1)
                depth_mapping[depth].append(node.val)
                recurse(node.right, depth + 1)

        recurse(root, 1)

        return [depth_mapping[k][-1] for k in sorted(depth_mapping.keys())]
