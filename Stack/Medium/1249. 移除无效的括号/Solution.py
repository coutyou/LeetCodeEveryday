class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        rm = {}
        for i, c in enumerate(s):
            if c == "(":
                stack.append((i, c))
            elif c == ")":
                if stack and stack[-1][1] == "(":
                    stack.pop()
                else:
                    rm[i] = True
    
        for i, c in stack:
            rm[i] = True

        res = ""
        for i in range(len(s)):
            if i not in rm:
                res += s[i]
        return res