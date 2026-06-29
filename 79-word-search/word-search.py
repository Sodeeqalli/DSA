class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        i = 0
        r,c = len(board), len(board[0])

        def backtrack(row, column, index):
            if index == len(word):
                return True
            
            if (row < 0 or column < 0 or row == r or column == c):
                return False
            
            if board[row][column] != word[index]:
                return False
            temp = board[row][column]
            board[row][column] = '#'
            up = backtrack(row-1,column,index+1)
            down =backtrack(row+1, column, index+1)
            right =backtrack(row, column+1, index+1)
            left = backtrack(row, column-1, index+1)
            board[row][column] = temp
            return up or down or right or left
        
        for aRow in range(r):
            for aCol in range(c):
                sol = backtrack(aRow, aCol, 0)
                if sol:
                    return True
        
        return False
            


        