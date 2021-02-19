# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack1 = [root]
        stack2 = []
        res = []
        level = 0
        while stack1 or stack2:
            if level & 1 == 0:
                node = stack1.pop()
                if level == len(res):
                    res.append([node.val])
                else:
                    res[-1].append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
                if not stack1:
                    level += 1
            else:
                node = stack2.pop()
                if level == len(res):
                    res.append([node.val])
                else:
                    res[-1].append(node.val)
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)
                if not stack2:
                    level += 1
        return res