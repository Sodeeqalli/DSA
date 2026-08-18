class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #basically for every island we dfs and mark cell as visited

        rowLen, colLen = len(grid), len(grid[0])
        visited = [[False for _ in range(colLen)] for _ in range(rowLen)]


        def dfs(row,col):
            if row < 0 or row == rowLen or col < 0 or col == colLen:
                return 0
            if visited[row][col] == True:
                return 0
            if grid[row][col]==0:
                return 0
            
            visited[row][col] = True

            left = dfs(row, col-1)
            right = dfs(row, col+1)
            up = dfs(row-1, col)
            down = dfs(row+1, col)

            return 1 + left + right + up + down

        maxArea = 0

        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 0 or visited[i][j] == True:
                    continue
                maxArea = max(maxArea, dfs(i,j))

        return maxArea