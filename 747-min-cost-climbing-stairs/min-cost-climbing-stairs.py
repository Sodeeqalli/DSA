class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        #cost  = curCost + min(step+1, step+2)
        #min cost from the last step is the cost of that step
        #min cost for the second to last is the the cost of that step and the cost of the last cause it cannot take 2 steps

        n = len(cost)
        minCost = [0] * n
        minCost[n-1] = cost[n-1]
        minCost[n-2] = cost[n-2]


        for i in range(n-3, -1, -1):
            minCost[i] = cost[i] + min(minCost[i+1], minCost[i+2])




        return min(minCost[0], minCost[1])

        