class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m,n = len(grid), len(grid[0])

        nextRow = [float("inf")] * (n+1)
        curRow = [float("inf")] * (n+1)

        #fill last roll
        nextRow[n-1] = grid[m-1][n-1]

        for col in range(n-2, -1, -1):
            nextRow[col] = grid[m-1][col] + nextRow[col+1]

        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                curRow[j] = grid[i][j] + min(curRow[j+1],nextRow[j])
            
            nextRow = curRow
        
        return nextRow[0]



