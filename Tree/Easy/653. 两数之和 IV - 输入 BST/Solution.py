# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        hash_ = {}
        self.dfs(root, hash_)
        for num in hash_.keys():
            if k-num in hash_ and k-num != num:
                return True
        return False

    def dfs(self, root, hash_):
        if root != None:
            self.dfs(root.left, hash_)
            hash_[root.val] = True
            self.dfs(root.right, hash_)