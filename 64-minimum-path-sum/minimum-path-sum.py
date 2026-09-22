class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        #dependence = current box + min(down, right)
        #bottom up
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[m-1][n-1] = grid[m-1][n-1]

        #fill last col
        for row in range(m-2, -1, -1):
            dp[row][n-1] = grid[row][n-1] + dp[row+1][n-1]
        
        #fill last row
        for col in range(n-2, -1, -1):
            dp[m-1][col] = grid[m-1][col] + dp[m-1][col+1]


        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

        
        return dp[0][0]
