class Solution:
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dp = [[float("inf") for _ in range(n+2)] for _ in range(n)]

        for j in range(n):
            dp[n-1][j+1] = grid[n-1][j]
     
        

        for r in range(n-2, -1, -1):
            for c in range(1, n+1):
                minimum = float("inf")
                for nextColumn in range(1,n+1):
                    if nextColumn == c:
                        continue
                    minimum = min(minimum,dp[r+1][nextColumn] ) 
                        
                dp[r][c] = grid[r][c-1] + minimum
        


        return min(dp[0])
        