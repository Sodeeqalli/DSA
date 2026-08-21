class Solution:
    def rob(self, nums: List[int]) -> int:
        #since adjacent cannot be robbed, we can either rob house 1 or start at house 2 since it can never be negative
        n = len(nums)
        memo = [None]*n

        def rob(i):
            if i >= n:
                return 0
            if memo[i] != None:
                return memo[i]
            
            maxValue = 0
            for j in range(i+2, n):
                value = rob(j)
                maxValue = max(value, maxValue)
            
            memo[i]= nums[i] + maxValue
            
            return memo[i]
        
        return max(rob(0), rob(1))


        