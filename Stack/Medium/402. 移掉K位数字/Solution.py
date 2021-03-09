class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        rm_num = 0
        stack = []
        for c in num:
            while stack and stack[-1] > c and rm_num < k:
                stack.pop()
                rm_num += 1
            stack.append(c)
        res = "".join(stack[:len(num)-k]).lstrip("0")
        return res if res else "0"