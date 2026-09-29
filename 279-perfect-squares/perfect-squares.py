class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        root = math.ceil(math.sqrt(n))
        

        for i in range(1,root+1):
            print(i)
            squares.append(i*i)
      
        memo = [None] * (n+1)
        def solve(i):
            if i > n:
                return float("inf")
            if i == n:
                return 0
            if memo[i] != None:
                return memo[i]

            minimum = float("inf")

            for j in range(len(squares)):
                minimum = min(minimum, solve(i+squares[j]))
            
            memo[i] = 1 + minimum

            return memo[i]

        return solve(0)

        


        