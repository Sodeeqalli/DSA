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
            
            take = nums[i] + rob(i+2)
            skip = rob(i+1)
            
            memo[i]= max(take, skip)

            return memo[i]
        
        return max(rob(0), rob(1))


        