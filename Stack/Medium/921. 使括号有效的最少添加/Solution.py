class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        res = 0
        stack = []
        for c in S:
            if c == "(":
                stack.append(c)
            else:
                if not stack:
                    res += 1
                else:
                    stack.pop()
        return res + len(stack)