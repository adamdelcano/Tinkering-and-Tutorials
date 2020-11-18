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
        # then find the smallest value for initializing the head/tail
        if not lists:
            return None
        next_val = float('inf')
        next_index = None
        purge_list = []  # So I don't have to modify list midloop
        for index, node in enumerate(lists):
            if not node:
                purge_list.append(index)
            elif node.val < next_val:
                next_val = node.val
                next_index = index
        # instantiate head and tail and new tail values
        try:
            merge_head = lists[next_index]
        except TypeError:
            return None
        merge_tail = merge_head
        # move to next node in the chosen linked list
        try:
            lists[next_index] = lists[next_index].next
        except AttributeError:  # if it was a one-entry list
            pass
        # cull empty linked lists
        while purge_list:
            del lists[purge_list.pop()]
        # collect smallest value every pass, use it for new tail
        while lists:
            next_val = float('inf')
            next_index = -1
            for index, node in enumerate(lists):
                if not node:
                    purge_list.append(index)
                elif node.val < next_val:
                    next_val = node.val
                    next_index = index
            if next_val == float('inf'):  # if the list was just a single None
                return merge_head
            new_tail = ListNode(next_val, next=None)
            merge_tail.next = new_tail
            merge_tail = new_tail
            try:
                lists[next_index] = lists[next_index].next
            except AttributeError:
                pass
            # cull empty linked lists
            while purge_list:
                del lists[purge_list.pop()]
        return merge_head
