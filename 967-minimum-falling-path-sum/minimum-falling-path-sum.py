class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        #this is basically cost of current + min (of next row +1 col+1, next row +1 col-1, next row +1 col)
        #so we solve later states first bottom up

        n = len(matrix)
        dp = [[float("inf") for _ in range(n+2)] for _ in range(n)]

        
        for col in range(n):
            dp[n-1][col+1] = matrix[n-1][col]
        
        for row in range(n-2, -1, -1):
            for col in range(n):
                dp[row][col+1] = matrix[row][col] + min(dp[row+1][col], dp[row+1][col+1], dp[row+1][col+2])

        return min(dp[0])
            
        