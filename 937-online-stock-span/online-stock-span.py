class StockSpanner:

    def __init__(self):
        self.stack = []
        self.days = []
        

    def next(self, price: int) -> int:
        dayCount = 1

        while self.stack and self.stack[-1] <= price:
            self.stack.pop()
            dayCount += self.days.pop()
        
        self.stack.append(price)
        self.days.append(dayCount)

        return dayCount

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)