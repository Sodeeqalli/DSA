class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,3,4]
        #[1,1,2,6]

        res = [1]*len(nums)
        
        forward = 1
        for i in range(1,len(res)):
            forward *= nums[i-1]
            res[i] = forward
        
        backward = 1
        for i in range(len(nums)-2, -1, -1):
            backward *= nums[i+1]
            res[i] *= backward
        
        return res