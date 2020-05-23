# for https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def _append_node(self, num: int) -> None:
        """Given a number, makes a new ListNode and appends it to the tail."""
        new_tail = ListNode(num)
        new_tail.next = None
        self.tail.next = new_tail
        self.tail = new_tail

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Given two non-empty linked lists representing two non-negative
        integers, that store the digits in reverse order, with each node
        containing a single digit. This function adds the numbers and returns
        it as a linked list."""
        # going to want to carry digits
        carried_num = 0
        # initialize head and tail and move other lists to next position
        self.head = ListNode(l1.val + l2.val)
        if self.head.val > 9:
            self.head.val -= 10
            carried_num = 1
        self.tail = self.head
        l1 = l1.next
        l2 = l2.next

        # Loop to take out the main body
        while l1 and l2:
            # upside of this version: no input validation needed inside loop
            # algo is pretty simple, just add the two and carry tens
            next_num = l1.val + l2.val + carried_num
            carried_num = 0
            if next_num > 9:
                next_num -= 10
                carried_num = 1
            self._append_node(next_num)
            # advance the lists
            l1 = l1.next
            l2 = l2.next
        # now to kill sin's left fin and right fin
        survivor = l1 if l1 else l2
        while survivor:
            # basically the same loop just without l2
            next_num = survivor.val + carried_num
            carried_num = 0
            if next_num > 9:
                next_num -= 10
                carried_num = 1
            self._append_node(next_num)
            survivor = survivor.next
        # taking out the core is easy
        if carried_num:
            self._append_node(carried_num)

        # finish
        return self.head
