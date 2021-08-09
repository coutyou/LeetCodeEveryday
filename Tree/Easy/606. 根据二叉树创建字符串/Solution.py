# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        if root == None:
            return ""
        res = str(root.val)
        if root.left == None and root.right == None:
            return res
        elif root.left == None:
            return res + "()(" + self.tree2str(root.right) + ")"
        elif root.right == None:
            return res + "(" + self.tree2str(root.left) + ")"
        else:
            return res + "(" + self.tree2str(root.left) + ")" + "(" + self.tree2str(root.right) + ")"