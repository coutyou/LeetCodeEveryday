class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        tmp = 0
        num = 0
        last_opr = "+"
        for c in s:
            if c == " ":
                pass
            elif c.isdigit():
                num = num * 10 + int(c)
            else:
                if last_opr == "+":
                    tmp += num
                elif last_opr == "-":
                    tmp -= num
                elif last_opr == "*":
                    tmp *= num
                elif last_opr == "/":
                    tmp = int(tmp / num)
                
                if c == "+" or c == "-":
                    res += tmp
                    tmp = 0

                last_opr = c
                num = 0

        if last_opr == "+":
            tmp += num
        elif last_opr == "-":
            tmp -= num
        elif last_opr == "*":
            tmp *= num
        elif last_opr == "/":
            tmp = int(tmp / num)

        res += tmp
        
        return res