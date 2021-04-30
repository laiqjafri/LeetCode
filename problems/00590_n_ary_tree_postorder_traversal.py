# 590. N-ary Tree Postorder Traversal
# Easy
#
# 966
#
# 74
#
# Add to List
#
# Share
# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
#
#
#
# Example 1:
#
#
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [5,6,3,2,4,1]
# Example 2:
#
#
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node, res = None) -> List[int]:
        if res is None:
            res = []

        if not root:
            return res

        for child in root.children:
            self.postorder(child, res)

        res.append(root.val)

        return res

    def postorder_iterative(self, root: Node):
        if not root:
            return []

        stack = []
        res = []

        stack.append(root)

        while stack:
            node = stack.pop()
            for child in node.children:
                stack.append(child)

            res.insert(0, node.val)

        return res
