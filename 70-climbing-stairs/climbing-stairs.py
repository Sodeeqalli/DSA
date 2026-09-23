class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] = dp[i+1] + dp[i+2]

        if n == 1:
            return 1

        twoStep = 0
        oneStep = 1



        for i in range(n-1, -1, -1):
            cur = oneStep + twoStep

            twoStep, oneStep = oneStep, cur

        return cur
