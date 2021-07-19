# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root, curPath, res):
            if curPath == "":
                curPath = str(root.val)
            else:
                curPath += "->" + str(root.val)
            if not root.left and not root.right:
                res.append(curPath)
                return res
            else:
                if root.left != None:
                    res = dfs(root.left, curPath, res)
                if root.right != None:
                    res = dfs(root.right, curPath, res)
                return res

        if root == None:
            return []
        return dfs(root, "", [])