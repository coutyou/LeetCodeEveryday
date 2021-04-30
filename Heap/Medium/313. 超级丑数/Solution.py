class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        from heapq import heappush, heappop
        
        res = [0 for _ in range(n+1)]
        res[1] = 1
        
        ptrs = [1 for _ in range(len(primes))]

        seen = {1}
        
        heap = []
        for i, p in enumerate(primes):
            heappush(heap, (p, i))
            seen.add(p)

        for i in range(2, n+1):
            num, idx = heappop(heap)
            res[i] = num
            ptrs[idx] += 1
            while res[ptrs[idx]] * primes[idx] in seen:
                ptrs[idx] += 1
            heappush(heap, (res[ptrs[idx]] * primes[idx], idx))
            seen.add(res[ptrs[idx]] * primes[idx])
            
        return res[n]

