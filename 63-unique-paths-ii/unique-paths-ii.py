class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[None for _ in range(n)] for _ in range(m)]

        def move(row, col):
            if row == m or col == n:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if row == m-1 and col == n-1:
                return 1
            if memo[row][col] != None:
                return memo[row][col]
            
            memo[row][col] = move(row+1, col) + move(row, col+1)

            return memo[row][col]

        
        return move(0,0)
            

            
        