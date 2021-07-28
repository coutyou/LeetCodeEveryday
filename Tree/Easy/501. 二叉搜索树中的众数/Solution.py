# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_freq = 0
        self.cur_freq = 0
        self.cur_num = None
        self.res = None

    def findMode(self, root: TreeNode) -> List[int]:
        self.dfs(root)
        if self.cur_freq == self.max_freq:
            self.res.append(self.cur_num)
        elif self.cur_freq > self.max_freq:
            self.res = [self.cur_num]
            self.max_freq = self.cur_freq
        return self.res
    
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.update(root.val)
        self.dfs(root.right)

    def update(self, val):
        if self.cur_num == None:
            self.cur_num = val
            self.cur_freq = 1
        else:
            if self.cur_num == val:
                self.cur_freq += 1
            else:
                if self.cur_freq == self.max_freq:
                    self.res.append(self.cur_num)
                elif self.cur_freq > self.max_freq:
                    self.res = [self.cur_num]
                    self.max_freq = self.cur_freq
                self.cur_num = val
                self.cur_freq = 1
