class StockSpanner:

    def __init__(self):
        self.stack = list()
        

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span = span + self.stack.pop()[1]
        self.stack.append([price, span])
        return span


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
for price in range(11):
    param_1 = obj.next(price)
    print(param_1)