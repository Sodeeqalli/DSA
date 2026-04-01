class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        stock = float("inf")

        for p in prices:
            if p > stock:
                profit += p - stock
            stock = p

        return profit


        