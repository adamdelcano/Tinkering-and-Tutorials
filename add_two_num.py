# for https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        """Doing a lot of single digit addition means carrying numbers"""
        self.carried_num = 0

    def _append_node(self, num: int) -> None:
        """Given a number, makes a new ListNode and appends it to the tail."""
        new_tail = ListNode(num)
        self.tail.next = new_tail
        self.tail = new_tail

    def _process_num(self, num: int) -> (int, int):
        """Given an integer, checks if it's over 10, then carries the tens
        digit."""
        self.carried_num = 0
        if num > 9:
            num -= 10
            self.carried_num = 1
        return num, self.carried_num

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Given two non-empty linked lists representing two non-negative
        integers, that store the digits in reverse order, with each node
        containing a single digit. This function adds the numbers and returns
        it as a linked list."""
        # going to want to carry digits
        # initialize head and tail and move other lists to next position
        self.head = ListNode(l1.val + l2.val)
        self.head.val = self._process_num(self.head.val)
        self.tail = self.head
        l1 = l1.next
        l2 = l2.next

        # Loop to take out the main body
        while l1 and l2:
            # add the numbers, process them, make new node with result
            next_num = l1.val + l2.val + self.carried_num
            next_num = self._process_num(next_num)
            self._append_node(next_num)
            # advance the lists
            l1 = l1.next
            l2 = l2.next
        # if one list is longer, this handles it
        survivor = l1 if l1 else l2
        while survivor:
            # basically the same loop just only need to add self.carried_num
            next_num = survivor.val + self.carried_num
            next_num = self._process_num(next_num)
            self._append_node(next_num)
            survivor = survivor.next
        # if last digits add to more than ten
        if self.carried_num:
            self._append_node(self.carried_num)

        # finish
        return self.head
