class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        p = 0
        for i in range(1, n+1):
            if p >= len(target):
                break
            elif target[p] > i:
                res.append("Push")
                res.append("Pop")
            else:
                res.append("Push")
                p += 1
        return res