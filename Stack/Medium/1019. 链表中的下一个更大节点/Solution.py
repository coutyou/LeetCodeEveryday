# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        res = []
        i = 0
        while head:
            while stack and stack[-1][0] < head.val:
                res[stack.pop()[1]] = head.val
            stack.append((head.val, i))

            head = head.next
            res.append(0)
            i += 1
        return res