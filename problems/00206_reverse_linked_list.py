# 206. Reverse Linked List
# Easy
#
# 6719
#
# 129
#
# Add to List
#
# Share
# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
#
# Input: head = []
# Output: []


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionIterative:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return head

        rev = ListNode( head.val )

        while head.next:
            head = head.next
            temp = rev
            rev = ListNode( head.val )
            rev.next = temp

        return rev


class SolutionRecursive:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return node