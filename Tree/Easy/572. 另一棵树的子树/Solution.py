# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root == None:
            return False
        if root.val == subRoot.val:
            return (self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, tree1, tree2):
        if tree1 == None and tree2 == None:
            return True
        elif tree1 == None or tree2 == None:
            return False
        else:
            if tree1.val != tree2.val:
                return False
            else:
                return self.isSameTree(tree1.left, tree2.left) and self.isSameTree(tree1.right, tree2.right)