class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)

        memo = defaultdict(lambda:None)

        def solve(i,holding):
            if i == n:
                return 0
            if memo[(i,holding)] != None:
                return memo[(i,holding)]


            if holding:
                skip = solve(i+1, True)
                sell = prices[i] - fee + solve(i+1, False)
                maximum = max(skip,sell)
            else:
                skip = solve(i+1, False)
                buy = -prices[i] + solve(i+1, True)
                maximum = max(skip,buy)

            memo[(i,holding)] = maximum

            return memo[(i,holding)]

        
        return solve(0, False)
