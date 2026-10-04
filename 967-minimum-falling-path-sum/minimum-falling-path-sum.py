class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        dp = [[0 for _ in range(n+2)] for _ in range(n)]

        for row in dp:
            row[0] = float("inf")
            row[-1] = float("inf")
    
        
        
        for j in range(n):
            dp[n-1][j+1] = matrix[n-1][j]
        

        for i in range(n-2,-1,-1):
            for j in range(1, n+1):
                dp[i][j] = matrix[i][j-1] + min(dp[i+1][j], dp[i+1][j+1], dp[i+1][j-1])
        
        return min(dp[0])


        