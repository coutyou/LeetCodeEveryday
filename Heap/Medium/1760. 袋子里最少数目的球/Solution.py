class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n = len(nums)
        sums = sum(nums)
        def dfs(mid):
            ans = 0
            for num in nums:
                ans += (num - 1) // mid
            return ans <= maxOperations

        left = max(sums // (n + maxOperations), 1)
        right = sums // maxOperations
        while left <= right:
            mid = (left + right) >> 1
            if dfs(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

