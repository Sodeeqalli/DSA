class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        memo = defaultdict(lambda: None)

        directions = [(-1,0),(1,0), (0,-1), (0,1)]

        def traverse(i, j, movesUsed):
            if movesUsed > maxMove:
                return 0
            if i == m or j == n or i == -1 or j == -1:
                return 1
            if memo[(i,j,movesUsed)] != None:
                return memo[(i,j,movesUsed)]
            
            numPaths = 0
            for rowDir,colDir in directions:
                numPaths += traverse(i+rowDir, j+colDir, movesUsed+1)

            memo[(i,j,movesUsed)] = numPaths

            return memo[(i,j,movesUsed)]

        
        return traverse(startRow, startColumn, 0) % (10**9 + 7)





            

            

        