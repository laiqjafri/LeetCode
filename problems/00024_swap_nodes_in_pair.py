# Given a linked list, swap every two adjacent nodes and return its head.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:
#
# Input: head = []
# Output: []
# Example 3:
#
# Input: head = [1]
# Output: [1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swap_pairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        old_head = head
        new_head = head.next

        old_head.next = self.swap_pairs(new_head.next)
        new_head.next = old_head
        return new_head
