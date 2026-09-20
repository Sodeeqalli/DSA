class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * (n+1)

        ways[n] = 1

        for i in range(n-1, -1, -1):
            oneStep = ways[i+1]
            twoStep = 0 if i+2 > n else ways[i+2]

            ways[i] = oneStep + twoStep
        
        return ways[0]


        