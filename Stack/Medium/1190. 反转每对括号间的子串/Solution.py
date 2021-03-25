class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack_char = []
        stack_num = []
        for c in s:
            if c == "(":
                stack_num.append(0)
            elif c == ")":
                tmp = ""
                for _ in range(stack_num.pop()):
                    tmp += stack_char.pop()[::-1]
                stack_char.append(tmp)
                if stack_num:
                    stack_num[-1] += 1
            else:
                stack_char.append(c)
                if stack_num:
                    stack_num[-1] += 1
        return "".join(stack_char)