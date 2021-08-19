"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.dfs(root)

    def dfs(self, root):
        if root == None:
            return 0
        else:
            max_dep = 0
            for c in root.children:
                dep = self.dfs(c)
                if dep > max_dep:
                    max_dep = dep
            return max_dep + 1