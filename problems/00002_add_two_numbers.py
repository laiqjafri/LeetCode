# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
#
#
# Example 1:
#
#
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
#
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:
#
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        node = None
        curr = None
        while l1 or l2:

            if l1 and l2:
                t = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                t = l1.val + carry
                l1 = l1.next
            elif l2:
                t = l2.val + carry
                l2 = l2.next

            total = t % 10
            carry = t // 10
            if not node:
                node = ListNode( total )
                curr = node
            else:
                curr.next = ListNode(total)
                curr = curr.next

        if carry:
            curr.next = ListNode( carry )

        return node
