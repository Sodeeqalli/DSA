class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        #we can start either from index 1 and index 0
        #so the initial state can be 0 or 1 not fixed (should we run the recursive function twice and find the min)
        #at every stage we pick 1 or 2, but since we want to return minimun cost, our function should return the min cost of if we take 1 or 2 steps
        #if we go beyond cost.length, then we return 0, if we are at cost.length we return the cost
        #welp we cant return 0 that will be the min cost
        #the problem now is how do we keep account of the costs
        #i am thinking now that the state is actually cost or like no the function is supposed to return cost
        
        n = len(cost)
        memo = [None] * n
        def climb(i):
            if i > n:
                return float("inf")
            if i == n:
                return 0
            if memo[i] != None:
                return memo[i]

            memo[i] = cost[i] + min(climb(i+1), climb(i+2))
            
            return memo[i]
        
        return min(climb(0), climb(1))

       

            





        
        