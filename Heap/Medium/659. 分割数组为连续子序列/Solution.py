class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        from heapq import heappush, heappop
        from collections import Counter
        countMap = Counter(nums)
        heap = []
        prev = 0
        prev_num = None
        for num in countMap:
            if prev_num != None and num - prev_num != 1:
                if -max(heap) < 3:
                    return False
                else:
                    heap = []
                    prev = 0
            if countMap[num] > prev:
                for i in range(len(heap)):
                    heap[i] -= 1
                for _ in range(countMap[num] - prev):
                    heappush(heap, -1)
            elif countMap[num] == prev:
                for i in range(len(heap)):
                    heap[i] -= 1
            else:
                for _ in range(prev - countMap[num]):
                    if -heappop(heap) < 3:
                        return False
                for i in range(len(heap)):
                    heap[i] -= 1
            prev = countMap[num]
            prev_num = num
        return -max(heap) >= 3