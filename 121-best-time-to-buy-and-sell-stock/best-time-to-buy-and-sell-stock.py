class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = float("inf")
        maxP = float("-inf")
        maxProfit = 0

        for p in prices:
            if p < minP:
                minP = p
                maxP = p
                continue
            if p > maxP:
                maxP = p
                maxProfit = max(maxProfit, maxP - minP)

        return maxProfit




