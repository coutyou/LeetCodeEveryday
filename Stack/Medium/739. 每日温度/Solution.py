class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                top = stack.pop()
                res[top] = i - top
            stack.append(i)
        return res