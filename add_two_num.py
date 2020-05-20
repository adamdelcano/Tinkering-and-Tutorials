# for https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # handle empty lists
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
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

        # Main loop to take out the main body
        while l1 and l2:
            # upside of this version: no input validation needed inside loop
            # algo is p simple, just add the two and carry tens
            next_num = l1.val + l2.val + carried_num
            carried_num = 0
            if next_num > 9:
                next_num -= 10
                carried_num = 1
            # make a new ListNode with the result and put it after tail
            new_tail = ListNode(next_num)
            new_tail.next = None
            self.tail.next = new_tail
            self.tail = new_tail
            # advance the lists
            l1 = l1.next
            l2 = l2.next
        # now to kill sin's left fin and right fin
        while l1:
            # basically the same loop
            next_num = l1.val + carried_num
            carried_num = 0
            if next_num > 9:
                next_num -= 10
                carried_num = 1
            new_tail = ListNode(next_num)
            new_tail.next = None
            self.tail.next = new_tail
            self.tail = new_tail
            l1 = l1.next
        while l2:
            # again basically the same loop
            next_num = l2.val + carried_num
            carried_num = 0
            if next_num > 9:
                next_num -= 10
                carried_num = 1
            new_tail = ListNode(next_num)
            new_tail.next = None
            self.tail.next = new_tail
            self.tail = new_tail
            l2 = l2.next
        # take out the core
        if carried_num:
            new_tail = ListNode(carried_num)
            new_tail.next = None
            self.tail.next = new_tail
            self.tail = new_tail
        # finish
        return self.head
