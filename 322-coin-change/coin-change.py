class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        memo = [None] * (amount+1)

        def solve(amountLeft):
            if amountLeft < 0:
                return float("inf")
            if amountLeft == 0:
                return 0
            if memo[amountLeft] != None:
                return memo[amountLeft]
            
            mini = float("inf")
            for coin in coins:
                numberOfCoins = 1 + solve(amountLeft - coin)
                mini = min(mini,numberOfCoins)
            
            memo[amountLeft] = mini
            
            return memo[amountLeft]
        
        answer = solve(amount)

        return -1 if answer == float("inf") else answer


        


        