# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root == None:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)
        while len(queue) != 0:
            total = 0
            n = len(queue)
            for _ in range(n):                 
                cur = queue.popleft()
                total += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(total / n)
        return res
