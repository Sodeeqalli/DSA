class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        #let me solve with recursion first
        m, n= len(triangle), len(triangle[-1])
        memo = [[None for _ in range(n)] for _ in range(m)] 

        def traverse(r,c):
            if r == m:
                return 0
            if memo[r][c] != None:
                return memo[r][c]
            
            memo[r][c] = triangle[r][c] + min(traverse(r+1,c), traverse(r+1,c+1))

            return memo[r][c]
        
        return traverse(0,0)


        