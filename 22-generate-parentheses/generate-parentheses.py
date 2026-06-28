class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, comb = [], []

        def backtrack(openn, close):
            if len(comb) == 2*n:
                res.append(''.join(comb))
                return

            
            if openn < n:
                comb.append('(')
                backtrack(openn+1,close)
                comb.pop()
            
            if close < openn:
                comb.append(')')
                backtrack(openn, close+1)
                comb.pop()

        backtrack(0, 0)
        return res


                
                    


        