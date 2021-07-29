# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
        self.min_dist = float("inf")

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.min_dist
    
    def dfs(self, root):
        if root == None:
            return
        self.dfs(root.left)
        
        if self.prev == None:
            self.prev = root.val
        else:
            self.min_dist = min(self.min_dist, abs(self.prev - root.val))
            self.prev = root.val 
        
        self.dfs(root.right)