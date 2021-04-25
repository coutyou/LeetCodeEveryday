class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_less = [-1] * n
        next_greater = [-1] * n

        stack = []
        idx_inc = sorted(range(n), key=lambda i: arr[i]) 
        for i in idx_inc:
            while stack and stack[-1] < i:
                next_greater[stack.pop()] = i
            stack.append(i)

        stack = []
        idx_dec = sorted(range(n), key=lambda i: -arr[i])
        for i in idx_dec:
            while stack and stack[-1] < i:
                next_less[stack.pop()] = i
            stack.append(i)

        dp = [[False for i in range(2)] for i in range(n)]
        dp[n-1][0], dp[n-1][1] = True, True
        res = 1

        for i in range(n-2, -1, -1):
            if next_greater[i] != -1 and dp[next_greater[i]][0] == True:
                dp[i][1] = True
                res += 1
            if next_less[i] != -1 and dp[next_less[i]][1] == True:
                dp[i][0] = True

        return res
