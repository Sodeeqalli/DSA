class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # memo = [None] * (amount+1)

        # def solve(amountLeft):
        #     if amountLeft < 0:
        #         return float("inf")
        #     if amountLeft == 0:
        #         return 0
        #     if memo[amountLeft] != None:
        #         return memo[amountLeft]
            
        #     mini = float("inf")
        #     for coin in coins:
        #         numberOfCoins = 1 + solve(amountLeft - coin)
        #         mini = min(mini,numberOfCoins)
            
        #     memo[amountLeft] = mini
            
        #     return memo[amountLeft]
        
        # answer = solve(amount)

        # return -1 if answer == float("inf") else answer

        #bottom up will be
        #state is amountLeft
        #for every state we try every coin and make the result of that state the minimum

        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):

            mini = float("inf")

            for coin in coins:
                numCoins = float("inf") if i - coin < 0 else 1 + dp[i-coin]
                mini = min(mini, numCoins)
            
            dp[i] = mini
        
        return -1 if dp[amount] == float("inf") else dp[amount]


        


        