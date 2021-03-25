class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = 0
        presum = [0]
        stack = [0]
        for h in hours:
            if h > 8:
                presum.append(presum[-1]+1)
            else:
                presum.append(presum[-1]-1)
        for i in range(len(presum)):
            if presum[i] < presum[stack[-1]]:
                stack.append(i)
        while stack and i > res:
            while stack and presum[stack[-1]] < presum[i]:
                res = max(res, i - stack[-1])
                stack.pop()
            i -= 1
        return res
        
        