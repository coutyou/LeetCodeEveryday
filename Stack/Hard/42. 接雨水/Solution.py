class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        res = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        while left <= right:
            if left_max > right_max:
                res += right_max - height[right]
                right -= 1
                if right >= 0:
                    right_max = max(right_max, height[right])
            else:
                res += left_max - height[left]
                left += 1
                if left <= len(height) - 1:
                    left_max = max(left_max, height[left])
        return res