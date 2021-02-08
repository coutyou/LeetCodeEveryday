class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        hash_ = {}
        stack = []
        res = []
        for num in nums2:
            if not stack or num < stack[-1]:
                stack.append(num)
            else:
                while stack and num > stack[-1]:
                    hash_[stack.pop()] = num
                stack.append(num)
        
        for num in nums1:
            if num in hash_:
                res.append(hash_[num])
            else:
                res.append(-1)
        
        return res