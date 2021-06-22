class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        for i in range(len(nums)):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i+1 >= k:
                while q and q[0] <= i-k:
                    q.popleft()
                res.append(nums[q[0]])
        return res
