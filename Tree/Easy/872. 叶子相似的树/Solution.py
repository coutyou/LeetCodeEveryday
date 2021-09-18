# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root):
            if root == None:
                return []
            res = []
            stack = [root]
            while stack:
                tmp = stack.pop()
                if not tmp.left and not tmp.right:
                    res.append(tmp.val)
                else:
                    if tmp.right:
                        stack.append(tmp.right)
                    if tmp.left:
                        stack.append(tmp.left)
            return res
        return dfs(root1) == dfs(root2)

