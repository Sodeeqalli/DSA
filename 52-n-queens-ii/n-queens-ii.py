class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        colPath = set()
        diagPath1 = set()
        diagPath2 = set()

        def backtrack(queens, row):
            nonlocal res
            if queens == n:
                res += 1
                return
            
            for col in range(n):
                if col in colPath or row-col in diagPath1 or row+col in diagPath2:
                    continue
                colPath.add(col)
                diagPath1.add(row-col)
                diagPath2.add(row+col)
                backtrack(queens+1, row+1)
                colPath.remove(col)
                diagPath1.remove(row-col)
                diagPath2.remove(row+col)
        
        backtrack(0,0)

        return res

        