# for https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def insert_after(self, target):  # I added this to cut code reuse
        new_node = ListNode(target)
        new_node.next = None
        self.next = new_node
        # Would like to put self = self.next here but the structure
        # of the problem does weird things


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
                self.tail.insert_after(l1.val)
                self.tail = self.tail.next
                l1 = l1.next
            else:
                self.tail.insert_after(l2.val)
                self.tail = self.tail.next
                l2 = l2.next
        # This approach leaves a straggler, must evacuate the remnants.
        while l1:
            self.tail.insert_after(l1.val)
            self.tail = self.tail.next
            l1 = l1.next
        while l2:
            self.tail.insert_after(l2.val)
            self.tail = self.tail.next
            l2 = l2.next

        # Purge Dummy Plug
        while self.head and self.head.val == 'Dummy Plug':
            self.head = self.head.next
        return self.head
