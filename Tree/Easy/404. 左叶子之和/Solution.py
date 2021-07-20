# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root.left:
            if not root.left.left and not root.left.right:
                left = root.left.val
            else:
                left = self.sumOfLeftLeaves(root.left)
        else:
            left = 0
        if root.right:
            right = self.sumOfLeftLeaves(root.right)
        else:
            right = 0
        return left + right