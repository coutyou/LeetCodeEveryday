# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        stack = []
        res = []
        while stack or root:
            while root:
                res.append(root.val)
                if root.right != None:
                    stack.append(root)
                root = root.left
            if stack:
                root = stack.pop().right
        return res
