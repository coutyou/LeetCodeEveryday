class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = []
        for num in stones:
            heapq.heappush(heap, -num)
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, min(first, second)-max(first, second))
        return -heap[0] if heap else 0