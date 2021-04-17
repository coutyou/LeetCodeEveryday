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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        ans = 0
        cnt = [0] * n

        for i in range(n):
            cnt[i] = int(matrix[0][i])
        ans = max(ans, self.largestRectangleArea(cnt))
        for j in range(1,m):
            for i in range(n):
                if matrix[j][i] == '1':
                    cnt[i] += 1
                else:
                    cnt[i] = 0
            ans = max(ans, self.largestRectangleArea(cnt))

        return ans