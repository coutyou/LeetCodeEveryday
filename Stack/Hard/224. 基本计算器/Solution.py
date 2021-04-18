class Solution:
    def calculate(self, s: str) -> int:
        opr_stack = [1]
        last_opr = 1
        res = 0
        i = 0
        while i < len(s):
            if s[i] == "(":
                opr_stack.append(last_opr * opr_stack[-1])
                last_opr = 1
                i += 1
            elif s[i] == ")":
                opr_stack.pop()
                i += 1
            elif s[i] == " ":
                i += 1
            elif s[i] == "+":
                last_opr = 1
                i += 1
            elif s[i] == "-":
                last_opr = -1
                i += 1
            else:
                tmp = 0
                while i < len(s) and s[i].isdigit():
                    tmp = tmp * 10 + int(s[i])
                    i += 1
                res += opr_stack[-1] * tmp * last_opr
        return res
                
