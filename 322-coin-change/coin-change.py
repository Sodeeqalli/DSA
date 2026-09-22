class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        #this seems similar to the combination problem where i have all states still available after picking one

        memo = [None] * (amount+1)


        def solve(curValue):
            if curValue > amount:
                return [-1,False]
            if curValue == amount:
                return [0,True]
            if memo[curValue] != None:
                return memo[curValue]
            
            #im struggling with how to keep count of coins taken so far
            #im struggling to model choices
            minimum = float("inf")
            reached = False
            for i in range(len(coins)):
                minFromI, reachedFromI = solve(curValue + coins[i])
                if reachedFromI and minFromI < minimum:
                    reached = reachedFromI
                    minimum = minFromI

            if reached == False:
                memo[curValue] = [-1, reached]
                return memo[curValue]

            memo[curValue] = [1 + minimum, reached]

            return memo[curValue]

        return solve(0)[0]



                
             
        