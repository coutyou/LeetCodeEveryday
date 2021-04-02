class MaxQueue:

    def __init__(self):
        self.queue = collections.deque()
        self.maxv = collections.deque()

    def max_value(self) -> int:
        if not self.queue: return -1
        else: return self.maxv[0]


    def push_back(self, value: int) -> None:
        while self.maxv and value > self.maxv[-1]:
            self.maxv.pop()
        self.maxv.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.queue: return -1
        ans = self.queue.popleft()
        if ans == self.maxv[0]: self.maxv.popleft()
        return ans



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()