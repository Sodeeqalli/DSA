class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        #this seems similar to the combination problem where i have all states still available after picking one

        memo = [None] * (amount+1)


        def solve(curValue):
            if curValue > amount:
                return float("inf")
            if curValue == amount:
                return 0
            if memo[curValue] != None:
                return memo[curValue]
            
            #im struggling with how to keep count of coins taken so far
            #im struggling to model choices
            minimum = float("inf")
            for i in range(len(coins)):
                minimum = min(solve(curValue + coins[i]), minimum)

            memo[curValue] = 1 + minimum
            return memo[curValue]

        fewest = solve(0)

        return fewest if fewest != float("inf") else -1



                
             
        