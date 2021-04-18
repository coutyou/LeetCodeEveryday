class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        last_opr = "+"
        for c in s:
            if c == " ":
                pass
            elif c.isdigit():
                num = num * 10 + int(c)
            elif last_opr == "+":
                stack.append(num)
                last_opr = c
                num = 0
            elif last_opr == "-":
                stack.append(-num)
                last_opr = c
                num = 0
            elif last_opr == "*":
                stack.append(stack.pop() * num)
                last_opr = c
                num = 0
            elif last_opr == "/":
                stack.append(int(stack.pop() / num))
                last_opr = c
                num = 0
        if last_opr == "+":
            stack.append(num)
        elif last_opr == "-":
            stack.append(-num)
        elif last_opr == "*":
            stack.append(stack.pop() * num)
        elif last_opr == "/":
            stack.append(int(stack.pop() / num))
        return sum(stack)