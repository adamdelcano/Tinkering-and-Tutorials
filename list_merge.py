# for https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge two sorted linked lists and return it as a new list.
        The new list should be made by splicing together the nodes of the
        first two lists."""
        # Check for empty lists
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2:
        elif l2 is None:
            return l1
        #Initialize head as smaller of l1/l2
        if l1.val < l2.val:
            self.head = l1 
            l1 = l1.next
        else: 
            self.head = l2
            l2 = l2.next
        #Initialize tail
        self.tail = self.head
        # Then go through both linked lists
        while l1 or l2:
            # If one is empty just add the other and stop
            if not l1:
                self.tail.next = l2
                break
            elif not l2:
                self.tail.next = l1
                break
            # Check which node goes next, then add it to tail.
            if l1.val <= l2.val:
                new_tail = ListNode(l1.val)
                new_tail.next = None
                self.tail.next = new_tail
                self.tail = new_tail
                l1 = l1.next
            else:
                new_tail = ListNode(l2.val)
                new_tail.next = None
                self.tail.next = new_tail
                self.tail = new_tail
                l2 = l2.next

        return self.head
