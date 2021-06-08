class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        from heapq import heappush, heappop
        heap = []
        sum_ = 0
        cur = 1
        pre_h = heights[0]
        for h in heights[1:]:
            if h > pre_h:
                if len(heap) < ladders:
                    heappush(heap, h-pre_h)
                else:
                    if heap and h-pre_h > heap[0]:
                        sum_ += heappop(heap)
                        heappush(heap, h-pre_h)
                    else:
                        sum_ += h-pre_h
                    if sum_ > bricks:
                        return cur - 1
            cur += 1
            pre_h = h
        else:
            return len(heights) - 1