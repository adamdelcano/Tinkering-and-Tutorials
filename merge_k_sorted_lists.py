# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [node for node in lists if node]
        lists.sort(key=lambda node:node.val)
        if not lists:
            return None
        merge_head = lists[0]
        merge_tail = merge_head
        try:
            lists[0] = lists[0].next
        except AttributeError:
            pass
        while lists:
            lists = [node for node in lists if node]
            if not lists:
                break
            lists.sort(key=lambda node:node.val)
            new_tail = ListNode(lists[0].val, next=None)
            merge_tail.next = new_tail
            merge_tail = new_tail
            lists[0] = lists[0].next
        return merge_head
                