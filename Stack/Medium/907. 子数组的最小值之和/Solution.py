class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        stack = [-1]
        res = 0
        for i in range(len(arr)):
            while len(stack) > 1 and arr[i] <= arr[stack[-1]]:
                top = stack.pop()
                res += arr[top] * (i-top) * (top-stack[-1])
            stack.append(i)
        return res % (10**9+7)