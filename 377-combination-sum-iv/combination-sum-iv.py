class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        #at every state, we still have all nums available for us to pick
        #so when we reach target, we return 1. if we exceed target we return zero
        #for this one the current index is not enough we need to know how much we have accumulated so far if we get to the same place through two different routes, the answer probably wont be the same
        n = len(nums)
        memo = [None] * target

        def combine(curSum):
            if curSum > target:
                return 0
            if curSum == target:
                return 1
            if memo[curSum] != None:
                return memo[curSum]
            
            ways = 0

            for i in range(n):
                ways += combine(curSum + nums[i])
            
            memo[curSum] = ways

            return memo[curSum]
        
        return combine(0)
                




        