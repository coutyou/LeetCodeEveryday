class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        from collections import defaultdict, deque
        outgraph = defaultdict(list)
        for (x,y,p) in flights:
            outgraph[x].append((p, y))
        que = deque()
        que.append((0, src))
        k = 0
        mintp = float('inf')
        dist = [float('inf') for _ in range(n)]
        dist[src] = 0
        while que and k <= K:
            size = len(que)
            for _ in range(size):
                cp, cur = que.popleft()
                for price,outplace in outgraph[cur]:
                    ncp = cp + price
                    if outplace == dst:
                        mintp = min(mintp,ncp)
                    elif ncp < dist[outplace]: 
                        que.append((ncp, outplace))
                        dist[outplace] = ncp
            k += 1
        return -1 if mintp == float('inf') else mintp