# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        elif root == p or root == q:
            return root
        else:
            left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
            if (left == p and right == q) or (left == q and right == p):
                return root
            elif right == None:
                return left
            else:
                return right
        