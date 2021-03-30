class Solution:
    def minInsertions(self, s: str) -> int:
        stack = 0
        i = 0
        res = 0
        while i < len(s):
            if s[i] == "(":
                stack += 1
            else:
                if stack == 0:
                    res += 1
                else:
                    stack -= 1
                if i + 1 < len(s) and s[i+1] == ")":
                    i += 1
                else:
                    res += 1
            i += 1
        return res + 2 * stack