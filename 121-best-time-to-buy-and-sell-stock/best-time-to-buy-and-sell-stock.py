class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy, maxSell = float("inf"), 0
        maxProfit = 0

        for p in prices:
            if p < minBuy:
                minBuy = p
                maxSell = p
            if p > maxSell:
                maxSell = p
                maxProfit = max(maxProfit, maxSell - minBuy)
        
        return maxProfit
        