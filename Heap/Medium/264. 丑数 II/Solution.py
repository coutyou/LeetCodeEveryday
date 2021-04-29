class Solution:
    def nthUglyNumber(self, n: int) -> int:
        from heapq import heappush, heappop
        heap = [1]
        cnt = 0
        got = {1}
        while cnt < n:
            num = heappop(heap)
            if not num*2 in got:
                heappush(heap, num*2)
                got.add(num*2)
            if not num*3 in got:
                heappush(heap, num*3)
                got.add(num*3)
            if not num*5 in got:
                heappush(heap, num*5)
                got.add(num*5)
            cnt += 1
        return num

