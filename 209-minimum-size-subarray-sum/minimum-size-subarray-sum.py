class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sumVal = 0
        l = 0
        minLen = float("inf")

        for r in range(len(nums)):
            sumVal+=nums[r]
            while l < len(nums) and sumVal >= target:
                minLen = min(minLen, r-l+1)
                sumVal-=nums[l]
                l+=1
            
        
        return 0 if minLen == float("inf") else minLen
        

        #[2,3,1,2,4,3]