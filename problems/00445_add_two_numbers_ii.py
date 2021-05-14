# 445. Add Two Numbers II
# Medium
#
# 2348
#
# 201
#
# Add to List
#
# Share
# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#
#
# Example 1:
#
#
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# Example 2:
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]
# Example 3:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []

        while l1 or l2:
            if l1:
                s1.append(l1.val)
                l1 = l1.next

            if l2:
                s2.append(l2.val)
                l2 = l2.next

        carry, head = 0, None
        while s1 or s2 or carry:
            d1 = s1.pop() if s1 else 0
            d2 = s2.pop() if s2 else 0

            carry, digit = divmod(d1 + d2 + carry, 10)

            new_head = ListNode(digit, head)
            head = new_head

        return head
