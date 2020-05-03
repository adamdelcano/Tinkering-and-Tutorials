# for https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# The process of making a new tail node should almost certainly be
# defined as a function. 

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Merge two sorted linked lists and return it as a new list.
        The new list should be made by splicing together the nodes of the
        first two lists."""
        # Initialize head and tail.
        self.head = ListNode('Dummy Plug')
        self.tail = ListNode('Dummy Plug')
        self.head.next = self.tail
        self.tail.next = None
        # Then go through both linked lists
        while l1 and l2:
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
        # This approach leaves a straggler, must evacuate the remnants.
        while l1:
            new_tail = ListNode(l1.val)
            new_tail.next = None
            self.tail.next = new_tail
            self.tail = new_tail
            l1 = l1.next
        while l2:
            new_tail = ListNode(l2.val)
            new_tail.next = None
            self.tail.next = new_tail
            self.tail = new_tail
            l2 = l2.next

        # Purge Dummy Plug
        while self.head and self.head.val == 'Dummy Plug':
                self.head = self.head.next
        return self.head
