class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if k == 0:
            return []
        from heapq import heappush, heappop
        heap = [(nums1[0]+nums2[0], 0, 0)]
        res = []
        seen = {(0, 0)}
        n = len(nums1)
        m = len(nums2)
        while heap and len(res) != k:
            _, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i < n and j+1 < m and (i, j+1) not in seen:
                heappush(heap, (nums1[i]+nums2[j+1], i , j+1))
                seen.add((i, j+1))
            if i+1 < n and j < m and (i+1, j) not in seen:
                heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
                seen.add((i+1, j))
        return res

