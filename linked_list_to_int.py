# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """Given head, which is a reference node to a singly-linked list.
        The value of each node in th linked list is either 0 or 1. The
        linked list holds the binary representation of a number. Returns
        the decimal value of the number."""
        num = ''
        while head:
            num += str(head.val)
            head = head.next
        return int(num, 2)
