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

        while l1 or l2 or carried_num:
            # acquires values from l1/l2, validating
            # would if: ... else be better here?
            try:
                first_num = l1.val
            except AttributeError:
                first_num = 0
            try:
                second_num = l2.val
            except AttributeError:
                second_num = 0
            # the actual algorithm: add them, check if >9, carry 1 if so
            next_num = first_num + second_num + carried_num
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
            try:
                l1 = l1.next
            except AttributeError:
                pass
            try:
                l2 = l2.next
            except AttributeError:
                pass
        # finish
        return self.head
