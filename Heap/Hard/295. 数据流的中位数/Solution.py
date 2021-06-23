class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        from heapq import heappush, heappop
        self.left = []
        self.right = []
        self.addLeft = True

    def addNum(self, num: int) -> None:
        if not self.left or num >= self.left[0]:
            heappush(self.left, num)
            if not self.addLeft:
                heappush(self.right, -heappop(self.left))
        else:
            heappush(self.right, -num)
            if self.addLeft:
                heappush(self.left, -heappop(self.right))
        self.addLeft = bool(1-self.addLeft)

    def findMedian(self) -> float:
        if self.addLeft:
            return (self.left[0] - self.right[0]) / 2
        else:
            return self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()