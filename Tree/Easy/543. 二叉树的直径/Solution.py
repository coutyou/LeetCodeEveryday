# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root == None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res = max(self.res, left+right)
        return max(left, right) + 1
