class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        memo = defaultdict(lambda: None)

        def solve(thrown,curSum):
            if curSum > target:
                return 0
            if curSum < target and thrown == n:
                return 0
            if curSum == target and thrown == n:
                return 1
            if memo[(thrown,curSum)] != None:
                return memo[(thrown, curSum)]
            
            ways = 0
            for side in range(1,k+1):
                ways += solve(thrown+1, curSum+side)

            memo[(thrown,curSum)] = ways

            return memo[(thrown, curSum)]

        return solve(0,0) % (10**9 + 7)





        