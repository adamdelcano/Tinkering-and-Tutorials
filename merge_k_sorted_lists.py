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

        # sanitize by removing empty linked lists, which are a possibility
        # then sort the list of linked lists by value
        lists = [node for node in lists if node]
        lists.sort(key=lambda node: node.val)
        if not lists:
            return None
        # instantiate head and tail
        merge_head = lists[0]
        merge_tail = merge_head
        # move to next node in the chosen linked list
        try:
            lists[0] = lists[0].next
        except AttributeError:  # if it was a one-entry list
            pass
        # cull empty linked lists
        lists = [node for node in lists if node]
        while lists:
            # sort the linked lists by node value, then add the smallest
            # as the tail and advance it
            lists.sort(key=lambda node: node.val)
            new_tail = ListNode(lists[0].val, next=None)
            merge_tail.next = new_tail
            merge_tail = new_tail
            lists[0] = lists[0].next
            # cull empty linked lists
            lists = [node for node in lists if node]
        return merge_head
