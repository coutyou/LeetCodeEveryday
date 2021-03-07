# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != "[":
            return NestedInteger(int(s))
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "[":
                cur = NestedInteger()
                stack.append(cur)
                i += 1
            elif s[i] == "]":
                stack.pop()
                if stack:
                    stack[-1].add(cur)
                    cur = stack[-1]
                i += 1
            elif s[i] == "-" or s[i].isdigit(): 
                num = int(s[i]) if s[i].isdigit() else 0
                neg = False if s[i].isdigit() else True
                i += 1
                while i < len(s):
                    if s[i] != "," and s[i] != "]":
                        num = num * 10 + int(s[i])
                        i += 1
                    else:
                        break
                if neg:
                    stack[-1].add(NestedInteger(-num))
                else:
                    stack[-1].add(NestedInteger(num))
            else:
                i += 1
        return cur


