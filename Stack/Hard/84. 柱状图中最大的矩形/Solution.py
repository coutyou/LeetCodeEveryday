class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_next_min = [-1] * n
        right_next_min = [n] * n
        
        stack = []
        i = 0
        while i < n:
            while stack and heights[stack[-1]] > heights[i]:
                right_next_min[stack.pop()] = i
            if stack:
                left_next_min[i] = stack[-1]
            stack.append(i)
            i += 1

        res = 0
        for i in range(n):
            res = max(res, (right_next_min[i] - left_next_min[i] - 1) * heights[i])
        return res