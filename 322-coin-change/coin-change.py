class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        #this seems similar to the combination problem where i have all states still available after picking one

        dp = [0] * (amount+1)

        dp[amount] = 0

        for i in range(amount-1, -1, -1):
            minimum = float("inf")

            for coin in coins:
                if coin + i <= amount:
                    minimum = min(1 + dp[coin+i], minimum)
            
            dp[i] = minimum
            
        return dp[0] if dp[0] != float("inf") else -1
               
                
             
        