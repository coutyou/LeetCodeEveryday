class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ""
        stack = []
        for idx, c in enumerate(S):
            if c == "(":
                stack.append((idx, c))
            else:
                if stack[-1][1] == "(" and len(stack) == 1:
                    res += S[stack[0][0]+1:idx]
                stack.pop()
        return res