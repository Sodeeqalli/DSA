class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [None]*(n+1)

        def climb(i):
            if i > n:
                return 0
            if memo[i] != None:
                return memo[i]
            if i == n:
                memo[i] = 1
                return 1
            
            memo[i] = climb(i+1) + climb(i+2)
            return memo[i]
        
        return climb(0)
            

        