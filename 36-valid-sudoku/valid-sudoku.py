class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = defaultdict(list)
        seenCol = defaultdict(list)
        seenGrid = defaultdict(list)
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val != ".":
                    if val in seenRow[row] or val in seenCol[col] or val in seenGrid[(row//3,col//3)]:
                        return False
                    seenRow[row].append(val)
                    seenCol[col].append(val)
                    seenGrid[(row//3,col//3)].append(val)
        
        return True
                    
                

        
        