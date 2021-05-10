class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)]
        dist = {num:float("inf") for num in range(1, n+1)}
        dist[k] = 0
        seen = set()
        while pq:
            d, node = heapq.heappop(pq)
            if node not in seen:
                seen.add(node)
                for nei, d2 in graph[node]:
                    if nei not in seen and d+d2 < dist[nei]:
                        dist[nei] = d + d2
                        heapq.heappush(pq, (d+d2, nei))

        max_ = max(dist.values())
        return max_ if max_ != float("inf") else -1
