class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #the only problem now is the fact that you can buy or sell at the same day but we should be able to handle
        n = len(prices)
        memo = defaultdict(lambda: None)


        def solve(i, holding):
            if i == n:
                return 0
            if memo[(i, holding)] != None:
                return memo[(i,holding)]

            maximum = 0
            if holding:
               wait = solve(i+1, True)
               sell = prices[i] + solve(i+1, False)
               maximum = max(wait,sell)
            else:
               wait = solve(i+1, False)
               buy = -prices[i] + solve(i+1, True)
               maximum = max(wait,buy)
            
            memo[(i,holding)] = maximum

            return memo[(i,holding)]


        return solve(0,False)
            