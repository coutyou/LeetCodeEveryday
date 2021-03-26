class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack_char = ["-1"]
        stack_num = ["-1"]
        for c in s:
            if c != stack_char[-1]:
                stack_char.append(c)
                stack_num.append(1)
            else:
                if stack_num[-1] == k-1:
                    stack_num.pop()
                    stack_char.pop()
                else:
                    stack_num[-1] += 1
        res = ""
        for c, n in zip(stack_char[1:], stack_num[1:]):
            res += c*n
        return res