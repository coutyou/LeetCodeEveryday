class Solution:
    def reorganizeString(self, s: str) -> str:
        from heapq import heappush, heappop
        from collections import Counter

        heap = [[-x[1], x[0]] for x in Counter(s).items()]
        heapq.heapify(heap)
        out = heappop(heap)
        res = [out[1]]
        out[0] += 1
        while heap:
            top = heappop(heap)
            res.append(top[1])
            top[0] += 1
            if out[0] != 0:
                heappush(heap, out)
            out = top
        if out[0] != 0:
            return ""
        return "".join(res)