class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # #let me solve with recursion first
        # m, n= len(triangle), len(triangle[-1])
        # memo = [[None for _ in range(n)] for _ in range(m)] 

        # def traverse(r,c):
        #     if r == m:
        #         return 0
        #     if memo[r][c] != None:
        #         return memo[r][c]
            
        #     memo[r][c] = triangle[r][c] + min(traverse(r+1,c), traverse(r+1,c+1))

        #     return memo[r][c]
        
        # return traverse(0,0)

        m, n = len(triangle), len(triangle[-1])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for col in range(n):
            dp[m-1][col] = triangle[m-1][col]
        
        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        
        return dp[0][0]




        