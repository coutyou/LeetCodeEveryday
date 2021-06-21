class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        from heapq import heappush, heappop
        heap = []
        res = []
        buildings_idx = 0
        last_height = 0

        key_points = []
        for b in buildings:
            key_points.append(b[0])
            key_points.append(b[1])
        key_points.sort()

        for p in key_points:
            while heap and heap[0][1] <= p:
                heappop(heap)

            while buildings_idx < len(buildings) and buildings[buildings_idx][0] == p:
                b = buildings[buildings_idx]
                heappush(heap, [-b[2], b[1]])
                buildings_idx += 1

            if not heap:
                max_height = 0
            else:
                max_height = -heap[0][0]

            if max_height != last_height:
                res.append([p, max_height])
                last_height = max_height

        return res