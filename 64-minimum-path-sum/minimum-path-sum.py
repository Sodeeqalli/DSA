class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[None for _ in range(n)] for _ in range(m)]


        def move(row,col):
            if row == m or col == n:
                return float("inf")
            
            if row == m-1 and col == n-1:
                return grid[row][col]

            if memo[row][col] != None:
                return memo[row][col]
            
            memo[row][col] = grid[row][col] + min(move(row+1, col), move(row, col+1))

            return memo[row][col]

        return move(0,0)



        