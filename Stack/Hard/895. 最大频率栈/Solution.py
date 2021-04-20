class FreqStack:
    def __init__(self):
        from collections import defaultdict
        self.max_freq = 0
        self.num2freq = defaultdict(int)
        self.freq2num = defaultdict(list)

    def push(self, val: int) -> None:
        self.num2freq[val] += 1
        self.freq2num[self.num2freq[val]].append(val)
        self.max_freq = max(self.num2freq[val], self.max_freq)

    def pop(self) -> int:
        num = self.freq2num[self.max_freq].pop()
        self.num2freq[num] -= 1
        if not self.freq2num[self.max_freq]:
            self.max_freq -= 1
        return num

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()