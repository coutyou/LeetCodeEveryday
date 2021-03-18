class StockSpanner:
    def __init__(self):
        self.res_stack = []
        self.price_stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.price_stack and self.price_stack[-1] <= price:
            top = self.price_stack.pop()
            res += self.res_stack.pop()
        self.price_stack.append(price)
        self.res_stack.append(res)
        return res
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)