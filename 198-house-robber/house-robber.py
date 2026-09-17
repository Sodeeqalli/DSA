class Solution:
    def rob(self, nums: list[int]) -> int:
        #the only state is the current house you are in
        #the decisions you can take is either rob the current house or not. if you rob current house you cant rob the next house, if you do not you might or might not rob the next house
        #if you go out of bounds we return 0
        n = len(nums)
        memo = [None] * n
        def robHouse(i):
            #if we pass the last house
            if i >= n:
                return 0
            if memo[i] != None:
                return memo[i]
            
            
            withCur = nums[i] + robHouse(i+2)
            withOutCur = robHouse(i+1)
        
            memo[i] =  max(withCur, withOutCur)

            return memo[i]
        
        return robHouse(0)



            
            
        