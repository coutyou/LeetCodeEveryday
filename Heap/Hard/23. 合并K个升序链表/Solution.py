# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from heapq import heappush, heappop
        heap = []
        for i,node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i))
                lists[i] = lists[i].next
        head = ListNode()
        cur = head
        while heap:
            val, i = heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        return head.next
