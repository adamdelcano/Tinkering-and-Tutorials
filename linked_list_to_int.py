# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode, base=2) -> int:
        """Given head, which is a reference node to a singly-linked list.
        The linked list holds representation of a number in given base,
        defaulting to binary. Returns the decimal value of the number."""
        num = 0
        while head:
            num *= base
            num += head.val
            head = head.next
        return num
