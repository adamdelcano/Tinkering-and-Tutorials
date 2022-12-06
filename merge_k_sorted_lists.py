# https://leetcode.com/problems/merge-k-sorted-lists
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        You are given an array of k linked-lists lists, each linked-list is
        sorted in ascending order.
        Merge all the linked-lists into one sorted linked-list and return it.

        Example 1:

        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        Explanation: The linked-lists are:
        [
            1->4->5,
            1->3->4,
            2->6
        ]
        merging them into one sorted list:
        1->1->2->3->4->4->5->6


        Example 2:
        Input: lists = []
        Output: []

        Example 3:
        Input: lists = [[]]
        Output: []

        Constraints:

        k == lists.length
        0 <= k <= 10^4
        0 <= lists[i].length <= 500
        -10^4 <= lists[i][j] <= 10^4
        lists[i] is sorted in ascending order.
        The sum of lists[i].length won't exceed 10^4.
        """
        # cheaty fast way: flatten everything into a reg list, sort it,
        # construct a new linked list
        node_vals = []
        for node in lists:
            while node:
                node_vals.append(node.val)
                try:
                    node = node.next
                except AttributeError:
                    pass
        if not node_vals:  # if empty input or [[]]
            return None
        node_vals.sort(reverse=True)
        merge_head = ListNode(node_vals.pop(), next=None)
        merge_tail = merge_head
        while node_vals:
            new_tail = ListNode(node_vals.pop(), next=None)
            merge_tail.next = new_tail
            merge_tail = new_tail
        return merge_head
