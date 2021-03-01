class Solution:
    def split(self, s):
        tmp = ""
        res = []
        for c in s:
            if c in ["+", "-", "*", "/"]:
                res.append(tmp)
                res.append(c)
                tmp = ""
            elif c == " ":
                continue
            else:
                tmp += c
        res.append(tmp)
        return res

    def calculate(self, s: str) -> int:
        s = self.split(s)
        stack = []
        flag = "+"
        last_opr = "+"
        for c in s:
            if c == "":
                continue
            elif c in ["+", "-"]:
                flag = c
                last_opr = c
            elif c in ["*", "/"]:
                last_opr = c
            else:
                num = int(c)
                if last_opr == "*":
                    top = stack.pop()
                    if flag == "+":
                        stack.append(top * num)
                    else:
                        stack.append(-top * num)
                        flag = "+"
                elif last_opr == "/":
                    top = stack.pop()
                    if flag == "+":
                        stack.append(int(top / num))
                    else:
                        stack.append(int(-top / num))
                        flag = "+"
                elif last_opr == "+":
                    stack.append(num)
                else:
                    stack.append(-num)
                    flag = "+"
        return sum(stack)