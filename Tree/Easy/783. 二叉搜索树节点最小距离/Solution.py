# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
        self.res = float("inf")

    def minDiffInBST(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if root != None:
            self.dfs(root.left)
            if self.prev != None:
                self.res = min(self.res, root.val-self.prev)
            self.prev = root.val
            self.dfs(root.right)