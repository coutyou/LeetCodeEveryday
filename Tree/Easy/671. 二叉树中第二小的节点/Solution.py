# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = self.dfs(root, root.val)
        return res if res != root.val else -1

    def dfs(self, root, base):
        if root.left == None and root.right == None:
            return root.val
        else:
            if root.left.val > base and root.right.val > base:
                return min(root.left.val, root.right.val)
            else:
                left = self.dfs(root.left, base)
                right = self.dfs(root.right, base)
                if left > base and right > base:
                    return min(left, right)
                else:
                    return max(left, right)