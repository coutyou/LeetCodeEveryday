class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = [""]
        num_stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                tmp = s[i]
                i += 1
                while s[i].isdigit():
                    tmp += s[i]
                    i += 1
                num_stack.append(int(tmp))
            elif s[i] == "[":
                str_stack.append("")
                i += 1
            elif s[i] == "]":
                top = str_stack.pop()
                str_stack[-1] += num_stack.pop() * top
                i += 1
            else:
                str_stack[-1] += s[i]
                i += 1
        return str_stack[-1]