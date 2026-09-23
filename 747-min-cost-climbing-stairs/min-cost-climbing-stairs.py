class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)

        twoAhead = 0
        oneAhead = cost[-1]

        if n == 1:
            return oneAhead

        for i in range(n-2, -1, -1):
            cur = cost[i] + min(oneAhead, twoAhead)

            twoAhead = oneAhead
            oneAhead = cur

        return min(oneAhead, twoAhead)


        