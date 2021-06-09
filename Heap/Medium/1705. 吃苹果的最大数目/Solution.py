class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        from heapq import heappush, heappop
        res = 0
        heap = []
        for i in range(len(apples)):
            if apples[i] != 0:
                heappush(heap, [i+days[i], apples[i]])
            while heap:
                if i < heap[0][0]:
                    break
                else:
                    heappop(heap)
            if heap:
                heap[0][1] -= 1
                res += 1
                if heap[0][1] == 0:
                    heappop(heap)
        while heap:
            i += 1
            while heap:
                if i < heap[0][0]:
                    break
                else:
                    heappop(heap)
            if heap:
                heap[0][1] -= 1
                res += 1
                if heap[0][1] == 0:
                    heappop(heap)
        return res