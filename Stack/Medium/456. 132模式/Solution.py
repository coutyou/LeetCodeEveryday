class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        min_ = [nums[0]]
        for num in nums[1:]:
            min_.append(min(min_[-1], num))
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > min_[i]:
                while stack and stack[-1] <= min_[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False