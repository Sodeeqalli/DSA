class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #from where we are, we need to find cheapest way to get to top
        #managing running costs from the two separate paths is my problem now
        n = len(cost)
        memo = [None]*(n+1)

        def climb(i):
            if i >= n:
                return 0
            if memo[i] != None:
                return memo[i]
            
            memo[i] = cost[i] + min(climb(i+1), climb(i+2))
        
            return memo[i]

        startOne = climb(0)
        memo = [None]*n
        startTwo = climb(1)
        
        return min(startOne, startTwo)




        