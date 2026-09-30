class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #state -> i, holding, transactionsUsed
        #choices -> if enough transactions left and  holding -> skip, sell
        #           if enough transactions left and not holding -> skip, buy
        #baseCases -> if we have usedAll transactions return 0
        #             if we are outside the bonds we cannot make any profit so return 0

        n = len(prices)
        memo = defaultdict(lambda:None)

        def solve(i,holding,transactionsUsed):
            if i == n:
                return 0
            if transactionsUsed == 2:
                return 0
            if memo[(i,holding,transactionsUsed)] != None:
                return memo[(i,holding,transactionsUsed)]

            if holding:
                skip = solve(i+1, True, transactionsUsed)
                sell = prices[i] + solve(i+1, False, transactionsUsed+1)
                maximum = max(skip,sell)
            else:
                skip = solve(i+1, False, transactionsUsed)
                buy = -prices[i] + solve(i+1, True, transactionsUsed)
                maximum = max(skip,buy)
            
            memo[(i,holding,transactionsUsed)] = maximum

            return memo[(i,holding,transactionsUsed)]

        return solve(0,False,0)



        