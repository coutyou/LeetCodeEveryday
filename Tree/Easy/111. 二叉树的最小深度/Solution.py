# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        import queue
        queue = queue.Queue()
        queue.put((root, 1))
        while queue:
            node, depth = queue.get()
            if node.left == None and node.right == None:
                return depth
            else:
                if node.left != None:
                    queue.put((node.left, depth+1))
                if node.right != None:
                    queue.put((node.right, depth+1))