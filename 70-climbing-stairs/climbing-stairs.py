class Solution:
    def climbStairs(self, n: int) -> int:
        twoAhead = 0
        oneAhead = 1

        for i in range(n-1, -1, -1):
            curState = oneAhead + twoAhead

            twoAhead = oneAhead
            oneAhead = curState
        

        return oneAhead
        