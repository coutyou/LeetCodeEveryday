class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        stack = []
        for c in s:
            if not stack or ord(stack[-1]) ^ ord(c) != 32:
                stack.append(c)
            else:
                stack.pop()
        return "".join(stack)