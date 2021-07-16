# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root:
                res.append(stack.pop().val)
            else:
                if not root.right:
                    res.append(root.val)
                    root = None
                else:
                    stack.append(root)
                    stack.append(None)
                    root = root.right
        return res