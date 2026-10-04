class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        #get length of row and column
        m, n = len(grid), len(grid[0])

        #dp table covering out of bound rows
        #also 0 for last state
        dp = [[0 for _ in range(n)] for _ in range(m+2)]
        
        #allowed row moves
        movement = [-1, 0, 1]

        #starting from second to last column, cause answer for last column all 0
        for c in range(n-2, -1, -1):
            #starting from 1st row to second to last for dp states
            for r in range(1, m+1):
                #initially set max to negative infinity
                maximum = float("-inf")
                #we check all moves
                for move in movement:
                    #if the move is out of bound cause we go up and down
                    #we move on to the next cause it is invalid
                    nextMove = r+move
                    if nextMove == 0 or nextMove == m+1:
                        continue
                    #for every valid move, we check if the original grid values of the next is greater than the original grid value of the current, if it is valid, we check and see if it has the maximum to the destination so far
                    if grid[nextMove-1][c+1] > grid[r-1][c]:
                        maximum = max(maximum, dp[nextMove][c+1])
                #at the end we check if we never came across a valid path, we set it to zero moves
                if maximum == float("-inf"):
                    dp[r][c] = 0
                #if we did come across a valid path, we set it to 1 move + the max move from the place we take
                else:
                    dp[r][c] = 1 + maximum
        
        #return max of the valid dp states in the first column
        return max(dp[row][0] for row in range(1,m+1))

                
        