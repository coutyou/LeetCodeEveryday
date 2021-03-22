class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 3 != 0:
            return False
        stack = []
        for c in s:
            if c == "a":
                stack.append(c)
            elif c == "b":
                if stack and stack[-1] == "a":
                    stack.append(c)
                else:
                    return False
            else:
                if len(stack) >= 2 and stack[-1] == "b" and stack[-2] == "a":
                    stack.pop()
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
