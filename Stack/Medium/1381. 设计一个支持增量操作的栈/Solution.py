class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.i = 0

    def push(self, x: int) -> None:
        if self.i != len(self.stack):
            self.stack[self.i] = x
            self.i += 1

    def pop(self) -> int:
        if self.i == 0:
            return -1
        else:
            res = self.stack[self.i-1]
            self.i -= 1
            return res

    def increment(self, k: int, val: int) -> None:
        k = min(k, self.i)
        for i in range(k):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)