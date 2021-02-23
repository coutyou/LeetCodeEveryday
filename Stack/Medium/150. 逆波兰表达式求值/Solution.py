class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                x2 = stack.pop()
                x1 = stack.pop()
                stack.append(x1 + x2)
            elif t == "-":
                x2 = stack.pop()
                x1 = stack.pop()
                stack.append(x1 - x2)
            elif t == "*":
                x2 = stack.pop()
                x1 = stack.pop()
                stack.append(x1 * x2)
            elif t == "/":
                x2 = stack.pop()
                x1 = stack.pop()
                stack.append(int(x1 / x2))
            else:
                stack.append(int(t))
        return stack[-1] if stack else 0